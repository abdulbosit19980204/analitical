// let clients = {{ gps|safe }}; // Backend-dan yuborilgan client ma'lumotlari
let clients = [{"latitude": 41.2995, "longitude": 69.2401, "name": "Client A"}, {
    "latitude": 41.3100, "longitude": 69.2700, "name": "Client B"
}, {"latitude": 41.3995, "longitude": 69.2801, "name": "Client A"}, {
    "latitude": 41.1995, "longitude": 69.2901, "name": "Client A"
},]


function initMap() {
    // Xaritani markazlash
    const mapCenter = {lat: 41.2995, lng: 69.2401}; // Default - Toshkent
    const map = new google.maps.Map(document.getElementById('map'), {
        zoom: 10, center: mapCenter,
    });
    fetch('/api/gps').then(response => response.json()).then(result => {
        gps = result['gps_data'];
        console.log(gps)

        // Mijozlar uchun marker joylash
        gps.forEach(gps => {
            // console.log(client)
            const clientLatLng = {
                lat: parseFloat(gps.latitude), lng: parseFloat(gps.longitude)
            };
            console.log(clientLatLng)
            new google.maps.Marker({
                position: clientLatLng, map: map, title: gps.name,
            });
        });
    })


}
