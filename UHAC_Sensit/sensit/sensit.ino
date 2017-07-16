#include <SPI.h>
#include <Ethernet.h>
#include <EthernetClient.h>
#include <EthernetServer.h>

float a[] = {0,0,0};

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(0, INPUT);
  pinMode(1, INPUT);
  pinMode(2, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int i;
  for (i=0; i<3; i++) {
    a[i] = analogRead(i);
    a[i] = a[i] / 1023 * 5;
  }
  Serial.print(a[0]);
  Serial.print(" ");
  Serial.print(a[1]);
  Serial.print(" ");
  Serial.println(a[2]);
  delay(3000);
}
