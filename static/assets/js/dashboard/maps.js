// let clients = {{ gps|safe }}; // Backend-dan yuborilgan client ma'lumotlari
let clients = [{"latitude": 41.2995, "longitude": 69.2401, "name": "Client A"}, {
    "latitude": 41.3100, "longitude": 69.2700, "name": "Client B"
}]

function initMap() {
    // Xaritani markazlash
    const mapCenter = {lat: 41.2995, lng: 69.2401}; // Default - Toshkent
    const map = new google.maps.Map(document.getElementById('map'), {
        zoom: 10, center: mapCenter,
    });

    // Mijozlar uchun marker joylash
    clients.forEach(client => {
        const clientLatLng = {
            lat: parseFloat(client.latitude), lng: parseFloat(client.longitude)
        };
        new google.maps.Marker({
            position: clientLatLng, map: map, title: client.name,
        });
    });
}
