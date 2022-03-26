
const srcPath = "../../static/images/";



// basemap
var map = new ol.Map({
    target: 'map',
    layers: [
    new ol.layer.Tile({
        source: new ol.source.OSM()
    })
    ],
    view: new ol.View({
    center: ol.proj.fromLonLat([6.30, 62.47]),
    zoom: 12.7
    })
});

var customStyleFunction = function(feature) {
    const file = feature.get('file');
    const path = srcPath + file +".jpg";
    
    return [new ol.style.Style({
    image: new ol.style.Photo ({
    src: path,
    radius: 30,
    shadow: true,
    stroke: new ol.style.Stroke({
        width: 1,
        color: '#fff'
    })
    })
})];
};


var vectorPhoto = new ol.layer.Vector({
    source: new ol.source.Vector({
    url:"../../static/js/alesund.geojson",
    format: new ol.format.GeoJSON(),
    }),
    style: customStyleFunction
});

map.addLayer(vectorPhoto);

var vectorShop = new ol.layer.Vector({ source: new ol.source.Vector() });

var shopMoa = new ol.Feature({
    geometry: new ol.geom.Point(ol.proj.fromLonLat([6.35, 62.467])),
    name: 'Moa',
    description: "aaaaaaaa",
});

vectorShop.getSource().addFeature(shopMoa);

var shopCentrum = new ol.Feature({
    geometry: new ol.geom.Point(ol.proj.fromLonLat([6.127, 62.467])),
    name: 'centrum',
    description: "bbbbbbb",
});

vectorShop.getSource().addFeature(shopCentrum);

var iconStyle = new ol.style.Style({
    image: new ol.style.Icon({
    opacity: 1,
    src: "../../static/images/bicycle.png",
    // <a href="https://www.flaticon.com/free-icons/bike" title="bike icons">Bike icons created by Those Icons - Flaticon</a>
    height:0.1,
    width:0.1,
    }),
    text: new ol.style.Text(
    {
        text: 'Bicycle store',
        scale: [2, 2],
        textAlign: 'center',
        textBaseline: 'top',
    }
    )
});
shopMoa.setStyle(iconStyle);
shopCentrum.setStyle(iconStyle);

map.addLayer(vectorShop);


// display window on click
map.on('click', function (evt) {
    const feature = map.forEachFeatureAtPixel(evt.pixel, function (feature) {
    return feature;
    });

    

    let mapInfo = document.getElementById('map-info-content');

    if (feature) {
    const name = feature.get('name');
    if (name == "Moa" || name == "centrum")
    {
        mapInfo.innerHTML=null;
        const h3 = document.createElement("h3");
        const p = document.createElement("p");
        h3.innerText = name;
        p.innerText = feature.get('description');
        mapInfo.appendChild(h3)
        mapInfo.appendChild(p)

    }
    else{
        const desc = feature.get('desc');
        const file = feature.get('file');
        const path = srcPath + file +".jpg";

        mapInfo.innerHTML=null;

        const img = document.createElement("img");
        const h3 = document.createElement("h3");
        const p = document.createElement("p");

        img.src = path;
        h3.innerText = name;
        p.innerText = desc;

        mapInfo.appendChild(img)
        mapInfo.appendChild(h3)
        mapInfo.appendChild(p)
    }
    


    }
});