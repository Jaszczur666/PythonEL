#include <Wire.h>
#include <MCP342x.h>

/* Demonstrate the use of convertAndRead().
*/


// 0x68 is the default address for all MCP342x devices
uint8_t address = 0x68;
MCP342x adc = MCP342x(address);

void setup(void)
{
  Serial.begin(9600);
  Wire.begin();

  // Reset devices
  MCP342x::generalCallReset();
  delay(1); // MC342x needs 300us to settle, wait 1ms

  // Check device present
  Wire.requestFrom(address, (uint8_t)1);
  if (!Wire.available()) {
    Serial.print("No device found at address ");
    Serial.println(address, HEX);
    while (1)
      ;
  }

}

void loop(void)
{
  long value = 0;
  MCP342x::Config status;
  while (Serial.available() == 0);
  char c = Serial.read();
  while (c != '\n') {
    c = Serial.read();
  }
  // Initiate a conversion; convertAndRead() will wait until it can be read
  uint8_t err = adc.convertAndRead(MCP342x::channel1, MCP342x::oneShot,
                                   MCP342x::resolution14, MCP342x::gain2,
                                   1000000, value, status);
  if (err) {
    Serial.print("Convert error: ");
    Serial.println(err);
  }
  else {
    //Serial.print("Value: ");
    Serial.println(value);
  }

  //delay(200);
}
