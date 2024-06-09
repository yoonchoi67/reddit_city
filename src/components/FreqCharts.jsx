import React, { useState, useEffect } from 'react';
import Chart from 'react-apexcharts';

function FreqCharts() {
    const [data, setData] = useState([]);

    const monthsOrder = [
        "January", "February", "March", 
        "April", "May", "June", 
        "July", "August", "September", 
        "October", "November", "December"
    ];

    const fetchData = () => {
        fetch('/submission_freq.json')
            // fetch('http://localhost:4001/submissions_frequency')
            .then(res => res.json())
            // .then(res => console.log(res))
            .then(res => res.submissions_frequency)
            .then(data => {
                const seriesData = Object.entries(data).map(([year, monthsData]) => ({
                    name: year,
                    data: monthsOrder.map(month => monthsData[month])
                }));
                setData(seriesData);
            })
            .catch(e => console.log(e.message));
    }
    
    useEffect(() => {
        fetchData();
    }, []);


    const chartOptions = {
        options: {
            chart: {
                height: 350,
                type: 'line',
                toolbar: { show: false },
            },
            markers: {
                size: 4,
            },
            colors: [
                "#FF0000",  //# Red
                "#FF7F00",  //# Red-Orange
                "#CCCC00",  //# Darker Yellow
                "#66CC00",  //# Darker Yellow-Green
                "#00CC00",  //# Darker Green
                "#00CC66",  //# Darker Blue-Green
                "#00CCCC",  //# Darker Cyan
                "#0066CC",  //# Darker Blue
                "#0000CC",  //# Darker Blue-Violet
                "#6600CC",  //# Darker Violet
                "#FF00FF",  //# Magenta
                "#FF007F"   //# Red-Violet
            ],
            fill: {
                type: 'gradient',
                gradient: {
                    shadeIntensity: 1,
                    opacityFrom: 1,
                    opacityTo: 1,
                    stops: [0,0,0]
                },
            },
            dataLabels: {
                enabled: false
            },
            stroke: {
                curve: 'smooth',
                width: 5,
            },
            xaxis: {
                categories: [
                    'January', 'February', 'March', 'April', 'May', 'June',
                    'July', 'August', 'September', 'October', 'November', 'December'
                ],
            },
        },
    };

    return (
        <div className="card">
            <div className="card-body">
                <h5 className='card-title'>
                    Frequency of Post Submission by Month
                    <Chart
                        options={chartOptions.options}
                        series={data}
                        type={chartOptions.options.chart.type}
                        height={chartOptions.options.chart.height}
                    />
                </h5>
            </div>
        </div>
    );
}

export default FreqCharts;
