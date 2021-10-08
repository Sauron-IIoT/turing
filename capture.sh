i=0
while [ $i -ne 10 ]
do
        i=$(($i+1))
        curl -o ./datasets/esp32_motor/validation/motor/$(uuidgen | tr "[:upper:]" "[:lower:]").jpg http://192.168.0.121/capture
done