// path for the map resources
const srcPath = "../../static/images/map/";


// creating basemap with Open Streen Map
var map = new ol.Map({
    target: 'map',
    layers: [
    new ol.layer.Tile({
        source: new ol.source.OSM()
    })
    ],
    view: new ol.View({
    center: ol.proj.fromLonLat([6.271, 62.47]),
    zoom: 11.5
    })
});

// creating style for photo points

var customStyleFunction = function(feature) {
    
    // taking photo path from geojson file and setting right file to the right photo
    const file = feature.get('file');
    const path = srcPath + file +"Icon.jpg";
    
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

// creating photo layer

var vectorPhoto = new ol.layer.Vector({
    source: new ol.source.Vector({
    url:"../../static/js/alesund.geojson",
    format: new ol.format.GeoJSON(),
    }),
    style: customStyleFunction
});

map.addLayer(vectorPhoto);

// creating shop layer with points

var vectorShop = new ol.layer.Vector({ source: new ol.source.Vector() });

var shopMoa = new ol.Feature({
    geometry: new ol.geom.Point(ol.proj.fromLonLat([6.35, 62.467])),
    name: 'Moa station',
    description: "Our rental point in Moa shop centre in the south building. We are open every day between 8:00 and 18:00, You can reserve bike via our page or buy on the place.",
});

vectorShop.getSource().addFeature(shopMoa);

var shopCentrum = new ol.Feature({
    geometry: new ol.geom.Point(ol.proj.fromLonLat([6.127, 62.467])),
    name: 'Centrum station',
    description: "Our rental point in city centre right next to the harbour. We are open every day between 8:00 and 18:00, You can reserve bike via our page or buy on the place.",
});

vectorShop.getSource().addFeature(shopCentrum);


// styling shop points

var iconStyle = new ol.style.Style({
    image: new ol.style.Icon({
    opacity: 1,
    src: "../../static/images/map/bike-shop.png",
    height:0.1,
    width:0.1,
    }),
});
shopMoa.setStyle(iconStyle);
shopCentrum.setStyle(iconStyle);

map.addLayer(vectorShop);





// display pop-up window on click on map feature
map.on('click', function (evt) {
    const feature = map.forEachFeatureAtPixel(evt.pixel, function (feature) {
    return feature;
    });

   
    let mapInfo = document.getElementById('map-info-content');

    // if in the place where the user clicked was any feature ( shop point or photo)
    // window display information regarding clicked point
    
    if (feature) {
        
        // takes feature name from the geojson file
        const name = feature.get('name');
        
        
       // different information are displayed for shop points and for photos
       // content for shops
        if (name == "Moa station" || name == "Centrum station")
        {
            // creating and appending needed elements
            mapInfo.innerHTML=null;
            const h3 = document.createElement("h3");
            const p = document.createElement("p");
            h3.innerText = name;
            p.innerText = feature.get('description');
            mapInfo.appendChild(h3)
            mapInfo.appendChild(p)
            
            // adding class for styling without photo
            mapInfo.classList.add("no-grid");
        }
        
        // content for photos
        else {
            
            // creating and appending needed elements
            const desc = feature.get('desc');
            const file = feature.get('file');
            const path = srcPath + file +".jpg";

            mapInfo.innerHTML=null;

            const img = document.createElement("img");
            const div = document.createElement("div");
            const h3 = document.createElement("h3");
            const p = document.createElement("p");

            img.src = path;
            h3.innerText = name;
            p.innerText = desc;

            mapInfo.appendChild(img)
            mapInfo.appendChild(div)
            div.appendChild(h3)
            div.appendChild(p)
            
            // adding class for styling with photo
            mapInfo.classList.remove("no-grid");
        }
    


    }
});
