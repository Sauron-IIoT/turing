i=0
while [ $i -ne 5 ]
do
        i=$(($i+1))
        curl -o ./datasets/fruits/tests/banana/$(uuidgen | tr "[:upper:]" "[:lower:]").jpg http://192.168.0.243/capture
done