i=0
while [ $i -ne 500 ]
do
        i=$(($i+1))
        curl -o ./datasets/esp32_motor/tests/esp32/$(uuidgen | tr "[:upper:]" "[:lower:]").jpg http://192.168.0.121/capture
done