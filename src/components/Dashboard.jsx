import React from 'react';
import './dashboard.css';
import './Leaflet';
import Leaflet from './Leaflet';
import FreqCharts from './FreqCharts';
import WorldTrafficChart from './WorldTrafficChart';
import UsaMap from './UsaMap';

function Dashboard() {
    
    return (
        <section className='dashboard section'>
            <div className='row'>
                <div className='col-lg-7'>
                    <div className='row'>
                        <div className='col-12'>
                            <Leaflet/>
                        </div>                    
                        <div className='col-12'>
                            <FreqCharts/>
                        </div>
                    </div>
                </div>
                <div className='col-lg-5'>

                    <div className='col-12'>
                        <WorldTrafficChart/>
                    </div>
                    <div className='col-12'>
                        <UsaMap/>
                    </div>
                        
                </div>
            </div>
            
        </section>
    )
}

export default Dashboard
