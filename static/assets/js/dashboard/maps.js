let clients = [{"latitude": 41.2995, "longitude": 69.2401, "name": "Client A"}, {
    "latitude": 41.3100, "longitude": 69.2700, "name": "Client B"
}, {"latitude": 41.3995, "longitude": 69.2801, "name": "Client C"}, {
    "latitude": 41.1995, "longitude": 69.2901, "name": "Client D"
},];

function initMap() {
    // Xaritani yaratish uchun boshlang'ich sozlamalar
    const mapCenter = {lat: 41.2995, lng: 69.2401}; // Toshkent markazi
    const map = new google.maps.Map(document.getElementById('map'), {
        zoom: 10, center: mapCenter,
    });

    // Geolokatsiyani olish
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (position) {
            const userLocation = {
                lat: position.coords.latitude, lng: position.coords.longitude,
            };

            // Xarita markazini foydalanuvchining joylashuviga o'rnatish
            map.setCenter(userLocation);

            // Foydalanuvchi uchun marker
            new google.maps.Marker({
                position: userLocation,
                map: map,
                title: "Sizning joylashuvingiz",
                icon: "http://maps.google.com/mapfiles/ms/icons/blue-dot.png", // Foydalanuvchiga alohida rang
            });

            // Har bir mijoz uchun yo'nalish chizish
            const directionsService = new google.maps.DirectionsService();
            const directionsRenderer = new google.maps.DirectionsRenderer({map: map});

            clients.forEach(client => {
                const clientLatLng = {
                    lat: parseFloat(client.latitude), lng: parseFloat(client.longitude),
                };

                // Yo'nalish so'rovini yuborish
                directionsService.route({
                    origin: userLocation, // Boshlang'ich nuqta foydalanuvchi joylashuvi
                    destination: clientLatLng, // Manzil mijoz joylashuvi
                    travelMode: google.maps.TravelMode.DRIVING, // Harakat turi
                }, function (response, status) {
                    if (status === google.maps.DirectionsStatus.OK) {
                        // Har bir yo'nalishni xaritada ko'rsatish
                        directionsRenderer.setDirections(response);
                    } else {
                        console.error("Yo'nalishni olishda xatolik yuz berdi: " + status);
                    }
                });
            });
        }, function () {
            alert("Lokatsiyani aniqlashga ruxsat berilmagan yoki xato yuz berdi!");
        });
    } else {
        alert("Geolokatsiya API brauzeringizda qo'llab-quvvatlanmaydi.");
    }
}
