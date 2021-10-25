i=0
while [ $i -ne 5 ]
do
        i=$(($i+1))
        curl -o ./datasets/esp32_motor/training/motor/$(uuidgen | tr "[:upper:]" "[:lower:]").jpg http://192.168.0.121/capture
done