var mymap = L.map('mapid').setView([42.0, -9.0], 2);

L.tileLayer('https://a.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    maxZoom: 18
}).addTo(mymap);

var markers = L.markerClusterGroup();

mymap.addLayer(markers);

arr.forEach(function(rec) {
    var marker = L.marker(new L.LatLng(rec.properties.lat_y, rec.properties.long_x));
    marker.bindPopup(
        '<b>Reddit Post Title:</b> ' + rec.properties.title + 
        '<br/><b>Gecoded into:</b> '+ rec.properties.display + 
        '<br/><b>Latitude: </b>'+rec.properties.lat_y+' <b>Longitude: </b>'+rec.properties.long_x +
        '<br/><b>Click <a href=\"https://reddit.com' + rec.properties.permalink+'\" target=\"_blank\">here</a> for the original post.</b>');
    markers.addLayer(marker);


})