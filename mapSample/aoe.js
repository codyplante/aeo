var mapOptions = {
    minZoom: 2,
    maxZoom: 4
};

var markerOptions = {
    radius: 2,
    fillColor: "#f48000",
    color: "#f48000",
    weight: 1,
    opacity: 1,
    fillOpacity: 0.7
};

var map = new L.Map('map', mapOptions);
var intervalId;

function onLoad() {

    document.getElementById("start").addEventListener("click", onClick);

    var baseLayer = L.tileLayer('http://{s}.basemaps.cartocdn.com/dark_nolabels/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> &copy; <a href="http://cartodb.com/attributions">CartoDB</a>',
        subdomains: 'abcd'
    }).addTo(map);

    locations.forEach(function (location) {
        location.marker = L.circleMarker(location.latLng, markerOptions).addTo(map);

        location.marker.on("mouseover", function (e) {
            location.marker.setStyle({
                fillOpacity: 0.95
            });
        });

        location.marker.on("mouseout", function (e) {
            location.marker.setStyle({
                fillOpacity: 0.7
            });
        });
    });

    map.setView([35, 0], 2);
}

function onClick() {
    var color = markerOptions.color;
    var fillColor = markerOptions.fillColor;
    var radius = markerOptions.radius;

    intervalId = setInterval(function () {

        radius = radius + 0.5;
        color = shadeColor(color, -0.01);
        fillColor = shadeColor(fillColor, -0.025);

        locations.forEach(function (location) {
            if ((location.duration + 1) * 6 > radius) {
                location.marker.setRadius(radius);
                location.marker.setStyle({
                    color: color,
                    fillColor: fillColor
                });
            }
        });

        if (radius > 25) {
            runComplete();
        }
    }, 50);
}

function runComplete() {
    clearInterval(intervalId);
}

function addText() {
    // Saving code
    location.text = L.marker(location.latLng, {
        icon: L.divIcon({
            className: 'text-label',
            html: location.duration.toString()
        })
    }).addTo(map);
}

function shadeColor(color, percent) {
    var f = parseInt(color.slice(1), 16), t = percent < 0 ? 0 : 255, p = percent < 0 ? percent * -1 : percent, R = f >> 16, G = f >> 8 & 0x00FF, B = f & 0x0000FF;
    return "#" + (0x1000000 + (Math.round((t - R) * p) + R) * 0x10000 + (Math.round((t - G) * p) + G) * 0x100 + (Math.round((t - B) * p) + B)).toString(16).slice(1);
}