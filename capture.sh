i=0
while [ $i -ne 100 ]
do
        i=$(($i+1))
        curl -o ./datasets/esp32_motor/tests/empty/$(uuidgen | tr "[:upper:]" "[:lower:]").jpg http://192.168.0.243/capture
done