void setup() {
        Serial.begin(9600);     // opens serial port, sets data rate to 9600 bps
}
int i = 0;
void loop() {
        String inByte = "";   // for incoming serial data
        // send data only when you receive data:
        if (Serial.available()) {
                // read the incoming byte:
                inByte = Serial.readString();
                if(inByte == "Ik wil bier")
                  Serial.println("Ik wil ook bier");
                else if(inByte == "Ik wil seks")
                  Serial.println("Ik wil ook seks");
                else{
                  Serial.println("Alleen voor 100 euro");
                }
                //Serial.println(buffer); 
                Serial.flush();
                //delay(1000);
        }
}
