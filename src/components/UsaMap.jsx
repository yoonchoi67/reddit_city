import React, { useEffect } from 'react';
import * as echarts from 'echarts';
import { GridComponent } from 'echarts/components';
import { MapChart } from 'echarts/charts';
import { TitleComponent, VisualMapComponent } from 'echarts/components';
import { CanvasRenderer } from 'echarts/renderers';

// Register echarts components
echarts.use([GridComponent, MapChart, TitleComponent, VisualMapComponent, CanvasRenderer]);

function UsaMap() {
    useEffect(() => {
        // Create an async function to fetch data
        const fetchData = async () => {
            try {
                // Fetch USA map data
                const response = await fetch('/usa.json');
                const usaMapData = await response.json();

                // Initialize chart DOM element
                const chartDom = document.getElementById('usaMap');
                const myChart = echarts.init(chartDom);
                
                // Show loading animation
                myChart.showLoading();

                // Register USA map
                // echarts.registerMap('USA', usaMapData);

                echarts.registerMap('USA', usaMapData, {
                    Alaska: {
                      // 把阿拉斯加移到美国主大陆左下方
                      left: -131,
                      top: 25,
                      width: 15
                    },
                    Hawaii: {
                      left: -110,
                      top: 28,
                      width: 5
                    },
                    'Puerto Rico': {
                      // 波多黎各
                      left: -76,
                      top: 26,
                      width: 2
                    }
                  });

                // Your data
                var data = [
                    { name: 'Alabama', value: 27 },
                    { name: 'Alaska', value: 32 },
                    { name: 'Arizona', value: 58 },
                    { name: 'Arkansas', value: 8 },
                    { name: 'California', value: 1124 },
                    { name: 'Colorado', value: 108 },
                    { name: 'Connecticut', value: 38 },
                    { name: 'Delaware', value: 6 },
                    { name: 'District of Columbia', value: 73 },
                    { name: 'Florida', value: 304 },
                    { name: 'Georgia', value: 118 },
                    { name: 'Hawaii', value: 35 },
                    { name: 'Idaho', value: 16 },
                    { name: 'Illinois', value: 1191 },
                    { name: 'Indiana', value: 61 },
                    { name: 'Iowa', value: 49 },
                    { name: 'Kansas', value: 45 },
                    { name: 'Kentucky', value: 36 },
                    { name: 'Louisiana', value: 46 },
                    { name: 'Maine', value: 21 },
                    { name: 'Maryland', value: 92 },
                    { name: 'Massachusetts', value: 316 },
                    { name: 'Michigan', value: 154 },
                    { name: 'Minnesota', value: 207 },
                    { name: 'Mississippi', value: 12 },
                    { name: 'Missouri', value: 144 },
                    { name: 'Montana', value: 26 },
                    { name: 'Nebraska', value: 21 },
                    { name: 'Nevada', value: 70 },
                    { name: 'New Hampshire', value: 8 },
                    { name: 'New Jersey', value: 88 },
                    { name: 'New Mexico', value: 16 },
                    { name: 'New York', value: 2347 },
                    { name: 'North Carolina', value: 91 },
                    { name: 'North Dakota', value: 35 },
                    { name: 'Ohio', value: 192 },
                    { name: 'Oklahoma', value: 26 },
                    { name: 'Oregon', value: 93 },
                    { name: 'Pennsylvania', value: 399 },
                    { name: 'Rhode Island', value: 29 },
                    { name: 'South Carolina', value: 33 },
                    { name: 'South Dakota', value: 7 },
                    { name: 'Tennessee', value: 78 },
                    { name: 'Texas', value: 315 },
                    { name: 'Utah', value: 39 },
                    { name: 'Vermont', value: 9 },
                    { name: 'Virginia', value: 82 },
                    { name: 'Washington', value: 415 },
                    { name: 'West Virginia', value: 16 },
                    { name: 'Wisconsin', value: 78 },
                    { name: 'Wyoming', value: 22 }
                ];


                // Sort data by value
                data.sort((a, b) => a.value - b.value);

                // Option for map chart
                const mapOption = {
                    visualMap: {
                        left: 'right',
                        min: 0,
                        max: 2500,
                        inRange: {
                            color: ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf', '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
                        },
                        text: ['High', 'Low'],
                        calculable: true
                    },
                    series: [
                        {
                            id: 'population',
                            type: 'map',
                            roam: true,
                            map: 'USA',
                            animationDurationUpdate: 1000,
                            universalTransition: true,
                            data: data
                        }
                    ]
                };

                // Option for bar chart
                const barOption = {
                    xAxis: {
                        type: 'value'
                    },
                    yAxis: {
                        type: 'category',
                        axisLabel: {
                            rotate: 30
                        },
                        data: data.map(item => item.name)
                    },
                    animationDurationUpdate: 1000,
                    series: {
                        type: 'bar',
                        id: 'population',
                        data: data.map(item => item.value),
                        universalTransition: true
                    }
                };

                // Set initial option to mapOption
                let currentOption = mapOption;
                myChart.setOption(mapOption);

                // Switch between map and bar chart every 2 seconds
                setInterval(() => {
                    currentOption = currentOption === mapOption ? barOption : mapOption;
                    myChart.setOption(currentOption, true);
                }, 5000);

                // Hide loading animation
                myChart.hideLoading();
            } catch (error) {
                console.error('Error fetching USA map data:', error);
            }
        };

        // Call the fetchData function
        fetchData();
    }, []);

    return (
        <div className="card">
            <div className="card-body">
                <h5 className='card-title'>
                    What US States were the pictures taken from?
                </h5>
                {/* Render chart container */}
                <div id='usaMap' style={{ minHeight: '400px' }} className='echart'></div>
            </div>
        </div>
    );
}

export default UsaMap;
