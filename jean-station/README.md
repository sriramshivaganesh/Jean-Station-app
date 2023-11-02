# Jean Station


This Repository contains the code for jean station app(similar to myntra), with react as the frontend, flask as backend and mongodb as the database. the backend is also docker containerized.

To start the project run the app.py and upload data of your wish using postman 

example json data is in the form of 


    {
        "name": "Leggin",
        "size": "L",
        "color": "Pink",
        "price": 1199.00,
        "id":32,
        "image_url": "https://th.bing.com/th/id/R.720c8b1efebe5a4f01b2308742161cb3?rik=HWvlIFbAYgvNHQ&riu=http%3a%2f%2fassets.myntassets.com%2fh_1440%2cq_95%2cw_1080%2fv1%2fimages%2fstyle%2fproperties%2fPannkh-Women-Pack-of-3-Churidar-Leggings_0543b9b579e98add62ffdacc2515cdbf_images.jpg&ehk=lj3bMeYeprsP73syA00mGwHVVO4K3ggKTFd4J0vZUxk%3d&risl=&pid=ImgRaw&r=0"
}

upload for both men and women seperately

to run react 
use commands 
npm install
npm start