import React, { useEffect } from 'react';
import * as echarts from 'echarts';

function WorldTrafficChart() {

  useEffect(() => {
    const chart = echarts.init(document.querySelector('#trafficChart'));

    // Sample data
    const data = [
      { value: 20287, name: 'N. America' },
      { value: 8487, name: 'Asia' },
      { value: 16017, name: 'Europe' },
      { value: 1282, name: 'S. America' },
      { value: 1360, name: 'Oceania' },
      { value: 699, name: 'Africa' }
    ];

    // Calculate total value
    const totalValue = data.reduce((acc, { value }) => acc + value, 0);

    chart.setOption({
      tooltip: {
        trigger: 'item',
        formatter: '{b}: {c} ({d}%)', // Show name, value, and percentage
      },
      legend: {
        top: '0%',
        left: 'center'
      },
      series: [
        {
          name: 'Access From',
          type: 'pie',
          radius: ['30%', '60%'],
          avoidLabelOverlap: true,
          label: {
            show: false,
            position: 'center',
          },
          emphasis: {
            label: {
              show: true,
              fontSize: '18',
              fontWeight: 'bold',
            },
          },
          labelLines: {
            show: false,
          },
          data: data.map(({ value, name }) => ({
            value,
            name,
            // Calculate percentage value
            percent: ((value / totalValue) * 100).toFixed(2),
          })),
        },
      ],
    });
  }, []);

  return (
    <div className="card">
      <div className="card-body">
        <h5 className='card-title'>
          What continents were the pictures taken from?
          <div
            id='trafficChart'
            style={{ minHeight: '300px' }}
            className='echart'>
          </div>
        </h5>
      </div>
    </div>
  );
}

export default WorldTrafficChart;
