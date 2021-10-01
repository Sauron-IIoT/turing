i=0
while [ $i -ne 300 ]
do
        i=$(($i+1))
        curl -o ./datasets/esp32_motor/training/empty/$(uuidgen | tr "[:upper:]" "[:lower:]").jpg http://192.168.0.243/capture
        sleep 1
done