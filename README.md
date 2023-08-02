# pingmyip.io

**[pingmyip.io](http://pingmyip.io)** is a free and open source API that allows you to check your public IP address. There are currently no limits on the number of calls you can make, but we ask that you keep calls within reason.

## Usage

The API currently returns both JSON and TXT. 

[JSON - pingmyip.io/json](https://pingmyip.io/json) 


[TXT - pingmyip.io/txt](https://pingmyip.io/txt) 


## Self-hosting

To self-host Pingmyip.io, you will need to have Docker installed. Once you have Docker installed, you can build the image and run the container.

### Build the image

```
docker build -t pingmyip
```

### Run the image

```
docker run --name pingmyip -d -p 4000:4000 -t pingmyip:latest
```

This will start a container with the pingmyip image and run it in detached mode. The container will listen on port 4000, so you can access the API by visiting http://localhost:4000 in your web browser.