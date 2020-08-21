// Interactive LED Panel Project
// Jake Martin & Eric Heising
// https://dl.espressif.com/dl/package_esp32_index.json, http://arduino.esp8266.com/stable/package_esp8266com_index.json in preferences=>board manager URLs
// Libraries: esp32, Coordinates, FastLED, Sparkfun Ambient Light Sensor Arduino
// Board: ESP32 Dev Module

// This sketch uses parts of libraries and example code from online documentation.
#include <FastLED.h>
#include <Wire.h>
#include <Coordinates.h>
#include "SparkFun_VEML6030_Ambient_Light_Sensor.h"
FASTLED_USING_NAMESPACE

// Include external project files
#include "Utils.h"
#include "Shapes.h"
struct Buffalo buff = {};

#if defined(FASTLED_VERSION) && (FASTLED_VERSION < 3001000)
#warning "Requires FastLED 3.1 or later; check github for latest code."
#endif

#define DATA_PIN    32
#define MICROPHONE  35
#define BUTTON_PIN  34
#define AL_ADDR   0x48
#define LED_TYPE    WS2811
#define COLOR_ORDER GRB
#define NUM_LEDS    500
#define LED_HALF    NUM_LEDS / 2

SparkFun_Ambient_Light light(AL_ADDR);
float gain = 0.125;
int Time = 100;
long luxVal = 0;

CRGB leds[NUM_LEDS];

int BRIGHTNESS = 200;
int FRAMES_PER_SECOND = 120;

uint8_t volume = 0;    //Holds the volume level read from the sound detector.
uint8_t last = 0;      //Holds the value of volume from the previous loop() pass.
uint16_t gradient = 0; //Used to iterate and loop through each color palette gradually
float maxVol = 15;     //Holds the largest volume recorded thus far to proportionally adjust the visual's responsiveness.
float avgVol = 0;      //Holds the "average" volume-level to proportionally adjust the visual experience.
float avgBump = 0;     //Holds the "average" volume-change to trigger a "bump."
bool bump = false;     //Used to pass if there was a "bump" in volume

int ledMode = 0;
int colorMode = 0;
byte prevButtonState = HIGH;
uint8_t gHue = 0; // rotating "base color" used by many of the patterns

void setup() {
  // put your setup code here, to run once:
  delay(3000); // 3 second delay for recovery
  Wire.begin();

  // tell FastLED about the LED strip configuration
  FastLED.addLeds<LED_TYPE,DATA_PIN,COLOR_ORDER>(leds, NUM_LEDS).setCorrection(TypicalLEDStrip);

  // set master brightness control
  FastLED.setBrightness(BRIGHTNESS);

  pinMode(BUTTON_PIN, INPUT);
  pinMode(MICROPHONE, INPUT);
  Serial.begin(9600);

  light.begin();
  light.setGain(gain);
  light.setIntegTime(Time);

  float gainVal = light.readGain();
  int timeVal = light.readIntegTime();
}

void loop()
{
  // send the 'leds' array out to the actual LED strip
  FastLED.show();
  // insert a delay to keep the framerate modest
  FastLED.delay(1000/FRAMES_PER_SECOND);

  luxVal = light.readLight();
  int temp = int(luxVal);
  Serial.println(temp);
  if(temp < 10)
  {
    FastLED.setBrightness(50);
  }
  else
  {
    FastLED.setBrightness(255);
  }
  // do some periodic updates
  EVERY_N_MILLISECONDS( 20 ) { gHue++; } // slowly cycle the "base color" through the rainbow

  byte buttonState = digitalRead(BUTTON_PIN);

  if( (prevButtonState == LOW) && (buttonState == HIGH) )
  {
    nextMode();
  }
  prevButtonState = buttonState;

  switch(ledMode)
  {
    case 0:
        FRAMES_PER_SECOND = 120;
        EVERY_N_SECONDS( 30 )
        {
          colorMode++;
          if( colorMode > 1 ) // Normally 12
          {
            colorMode = 0;
          }
        }
        switch(colorMode)
        {
           case 0:
              spiral();
              break;
           case 1:
              buff2();
              break;
           case 2:
              buff3();
              break;
           case 3:
              confetti();
              break;
           case 4:
              wow();
              break;
           case 5:
              sinelon();
              break;
           case 6:
              buffonecard();
              break;
           case 7:
              buff2_muted();
              break;
           case 8:
              bpm3();
              break;
           case 9:
              wow_hype();
              break;
           case 10:
              sinelon2();
              break;
           case 11:
              bpm8();
              break;
           case 12:
              bpm7();
              break;
        }
        break;

    case 1:
        FRAMES_PER_SECOND = 40;
        volume = analogRead(MICROPHONE);       //Record the volume level from the sound detector
        avgVol = (avgVol + volume) / 2.0;     //Take our "average" of volumes.

        //  Also if the volume is less than average volume / 2 (essentially an average with 0), it's considered silent.
        if (volume < avgVol / 2.0 || volume < 15) volume = 0;
        //If the current volume is larger than the loudest value recorded, overwrite
        if (volume > maxVol) maxVol = volume;
        //This is where "gradient" is reset to prevent overflow.
        if (gradient > 1529) {
          gradient %= 1530;
          //Everytime a palette gets completed is a good time to readjust "maxVol," just in case
          //  the song gets quieter; we also don't want to lose brightness intensity permanently
          //  because of one stray loud sound.
          maxVol = (maxVol + volume) / 2.0;
        }
        //If there is a decent change in volume since the last pass, average it into "avgBump"
        if (volume - last > avgVol - last && avgVol - last > 0) avgBump = (avgBump + (volume - last)) / 2.0;
        //if there is a notable change in volume, trigger a "bump"
        bump = (volume - last) > avgBump;

        sound1();
        gradient++;

        last = volume; //Records current volume for next pass

        break;

    case 2:
        FRAMES_PER_SECOND = 40;
        // put your main code here, to run repeatedly:
        volume = analogRead(MICROPHONE);       //Record the volume level from the sound detector
        avgVol = (avgVol + volume) / 2.0;     //Take our "average" of volumes.

        //  Also if the volume is less than average volume / 2 (essentially an average with 0), it's considered silent.
        if (volume < avgVol / 2.0 || volume < 15) volume = 0;
        //If the current volume is larger than the loudest value recorded, overwrite
        if (volume > maxVol) maxVol = volume;
        //This is where "gradient" is reset to prevent overflow.
        if (gradient > 1529) {
          gradient %= 1530;
          //Everytime a palette gets completed is a good time to readjust "maxVol," just in case
          //  the song gets quieter; we also don't want to lose brightness intensity permanently
          //  because of one stray loud sound.
          maxVol = (maxVol + volume) / 2.0;
        }
        //If there is a decent change in volume since the last pass, average it into "avgBump"
        if (volume - last > avgVol - last && avgVol - last > 0) avgBump = (avgBump + (volume - last)) / 2.0;
        //if there is a notable change in volume, trigger a "bump"
        bump = (volume - last) > avgBump;

        sound2();
        gradient++;

        last = volume; //Records current volume for next pass

        break;

    case 3:
        off();
        break;
  }
}

void off()
{
  fadeToBlackBy( leds, NUM_LEDS, 10);
}

void sound1()
{
    fade(0.75);   //Listed below, this function simply dims the colors a little bit each pass of loop()

    //Advances the gradient to the next noticeable color if there is a "bump"
    if (bump) gradient += 64;

    //If it's silent, we want the fade effect to take over, hence this if-statement
    if (volume > 0) {
        CRGB col = Rainbow(gradient); //Our retrieved 32-bit color;
        //These variables determine where to start and end the pulse since it starts from the middle of the strand.
        //  The quantities are stored in variables so they only have to be computed once.
        int start = LED_HALF - (LED_HALF * (volume / maxVol));
        int finish = LED_HALF + (LED_HALF * (volume / maxVol)) + NUM_LEDS % 2;
        //Listed above, LED_HALF is simply half the number of LEDs on your strand. ↑ this part adjusts for an odd quantity.

        for (int i = start; i < finish; i++) {

            //"damp" creates the fade effect of being dimmer the farther the pixel is from the center of the strand.
            //  It returns a value between 0 and 1 that peaks at 1 at the center of the strand and 0 at the ends.
            float damp = float(((finish - start) / 2.0) - abs((i - start) - ((finish - start) / 2.0))) / float((finish - start) / 2.0);
            //Sets the each pixel on the strand to the appropriate color and intensity
            //  strand.Color() takes 3 values between 0 & 255, and returns a 32-bit integer.
            //  Notice "knob" affecting the brightness, as in the rest of the visuals.
            //  Also notice split() being used to get the red, green, and blue values.
            leds[i] = CRGB(split(col, 0) * pow(damp, 2.0), split(col, 1) * pow(damp, 2.0), split(col, 2) * pow(damp, 2.0));
        }
    }
}

void sound2()
{
    fade(0.75);   //Listed below, this function simply dims the colors a little bit each pass of loop()

    //Advances the gradient to the next noticeable color if there is a "bump"
    if (bump) gradient += 64;

    //If it's silent, we want the fade effect to take over, hence this if-statement
    if (volume > 0) {
        CRGB col = Rainbow(gradient); //Our retrieved 32-bit color;
        //These variables determine where to start and end the pulse since it starts from the middle of the strand.
        //  The quantities are stored in variables so they only have to be computed once.
        int start = LED_HALF - (LED_HALF * (volume / maxVol));
        int finish = LED_HALF + (LED_HALF * (volume / maxVol)) + NUM_LEDS % 2;
        //Listed above, LED_HALF is simply half the number of LEDs on your strand. ↑ this part adjusts for an odd quantity.

        for (int i = start; i < finish; i++) {

            //"damp" creates the fade effect of being dimmer the farther the pixel is from the center of the strand.
            //  It returns a value between 0 and 1 that peaks at 1 at the center of the strand and 0 at the ends.
            float damp = float(((finish - start) / 2.0) - abs((i - start) - ((finish - start) / 2.0))) / float((finish - start) / 2.0);
            damp *= 2;
            //Sets the each pixel on the strand to the appropriate color and intensity
            //  strand.Color() takes 3 values between 0 & 255, and returns a 32-bit integer.
            //  Notice "knob" affecting the brightness, as in the rest of the visuals.
            //  Also notice split() being used to get the red, green, and blue values.
            leds[i] = CRGB(split(col, 0) * pow(damp, 2.0), split(col, 1) * pow(damp, 2.0), split(col, 2) * pow(damp, 2.0));
        }
    }
}

//Fades lights by multiplying them by a value between 0 and 1 each pass of loop().
void fade(float damper)
{
    //"damper" must be between 0 and 1, or else you'll end up brightening the lights or doing nothing.
    if (damper >= 1) damper = 0.99;

    for (int i = 0; i < NUM_LEDS; i++) {

      //Retrieve the color at the current position.
      CRGB col = (leds[i]) ? leds[i] : CRGB(0, 0, 0);

      //If it's black, you can't fade that any further.
      if (col == CRGB(0, 0, 0)) continue;

      float colors[3]; //Array of the three RGB values

      //Multiply each value by "damper"
      for (int j = 0; j < 3; j++) colors[j] = split(col, j) * damper;

      //Set the dampened colors back to their spot.
      leds[i] = CRGB(colors[0] , colors[1], colors[2]);
    }
}
uint8_t split(CRGB color, uint8_t i )
{
    //0 = Red, 1 = Green, 2 = Blue
    if (i == 0) return color[0];
    if (i == 1) return color[1];
    if (i == 2) return color[2];
    return -1;
}
//This function simply take a value and returns a gradient color
//  in the form of an unsigned 32-bit integer

//The gradient returns a different, changing color for each multiple of 255
//  This is because the max value of any of the 3 LEDs is 255, so it's
//  an intuitive cutoff for the next color to start appearing.
//  Gradients should also loop back to their starting color so there's no jumps in color.
CRGB Rainbow(unsigned int i) {
  if (i > 1529) return Rainbow(i % 1530);
  if (i > 1274) return CRGB(255, 0, 255 - (i % 255));   //violet -> red
  if (i > 1019) return CRGB((i % 255), 0, 255);         //blue -> violet
  if (i > 764) return CRGB(0, 255 - (i % 255), 255);    //aqua -> blue
  if (i > 509) return CRGB(0, 255, (i % 255));          //green -> aqua
  if (i > 255) return CRGB(255 - (i % 255), 255, 0);    //yellow -> green
  return CRGB(255, i, 0);                               //red -> yellow
}

void nextMode()
{
    ledMode++;
    if( ledMode > 3 )
    {
      ledMode = 0;
    }
}

int ring_rad = 1;
int offs = 0;
void spiral()
{
  for(int r=0; r<ring_rad; r++)
  {
    Coordinates point = Coordinates();
    point.fromPolar(r/20, r);
    int x = point.getX() - 1 + 12;
    int y = 19 - (point.getY() - 1 + 10);
    if(y%2 == 1)
    {
      x = 24-x;
    }
    int pos = int(x + (25 * y));
    if(pos < NUM_LEDS && pos >= 0)
    {
      leds[pos] = CHSV( (offs + r) % 256, 255, 150);
      offs++;
    }
    else
    {
      ring_rad = 1;
      break;
    }
  }
  ring_rad++;
  fadeToBlackBy( leds, NUM_LEDS, 25);

}

int buff_outer[][2] = { {25, 7}, {25, 8}, {25, 9}, {25, 10}, {25, 11}, {24, 12}, {24, 13}, {23, 13}, {23, 14}, {22, 15}, {21, 16}, {20, 16}, {19, 16}, {18, 16}, {17, 17}, {16, 18}, {15, 19}, {14, 19}, {13, 19}, {12, 19}, {12, 18}, {12, 17}, {11, 17},
                          {10, 16}, {9, 16}, {8, 16}, {7, 16}, {6, 16}, {6, 15}, {5, 15}, {5, 16}, {5, 17}, {5, 18}, {4, 19}, {3, 20}, {2, 20}, {2, 19}, {1, 18}, {1, 17}, {1, 16}, {2, 15}, {2, 14}, {2, 13}, {2, 12}, {3, 11}, {3, 10}, {3, 9}, {3, 8}, {4, 7},
                          {5, 6}, {6, 5}, {7, 5}, {8, 4}, {9, 3}, {10, 2}, {11, 2}, {12, 1}, {13, 1}, {14, 1}, {15, 1}, {16, 1}, {17, 2}, {18, 2}, {19, 3}, {20, 4}, {21, 4}, {22, 5}, {23, 5}, {24, 6}, {24, 7} };
int buff_C[][2] = { {14, 6}, {14, 5}, {13, 5}, {13, 6}, {12, 6}, {12, 5}, {11, 5}, {11, 6}, {10, 6}, {10, 5}, {9, 5}, {9, 6}, {8, 6}, {9, 7}, {8, 7}, {9, 8}, {8, 8}, {9, 9}, {8, 9}, {9, 10}, {8, 10}, {9, 11}, {8, 11}, {9, 12}, {10, 12},
                          {10, 11}, {11, 11}, {11, 12}, {12, 12}, {12, 11}, {13, 11}, {13, 12}, {14, 12}, {14, 11} };
int buff_U[][2] = { {11, 8}, {12, 8}, {11, 9}, {12, 9}, {11, 10}, {12, 10}, {11, 13}, {12, 13}, {11, 14}, {12, 14}, {12, 15}, {13, 14}, {13, 15}, {14, 15}, {14, 14}, {15, 14}, {15, 15}, {16, 15}, {16, 14}, {17, 14}, {16, 13}, {17, 13}, {16, 12}, {17, 12},
                          {16, 11}, {17, 11}, {16, 10}, {17, 10}, {16, 9}, {17, 9}, {16, 8}, {17, 8} };
int buff_horn[][2] = { {20, 11}, {21, 11}, {20, 10}, {21, 10}, {21, 9}, {22, 8} };
CRGB buff_col = CRGB(180, 180, 25);
int col_start = 0;
void buffonecard()
{
  //Buff background
  for(int i=0; i<NUM_LEDS; i++)
  {
    leds[i] = CRGB(10, 10, 10);
  }

  //Buff outline
  int col = col_start;
  for(int i=0; i<70; i++)
  {
    int x = buff_outer[i][0] - 1;
    int y = 19 - (buff_outer[i][1] - 1);

    if(y%2 == 1)
    {
      x = 24-x;
    }

    leds[x + (25*y)] = buff_col;
  }
  //Buff C
  for(int i=0; i<34; i++)
  {
    int x = buff_C[i][0] - 1;
    int y = 19 - (buff_C[i][1] - 1);

    if(y%2 == 1)
    {
      x = 24-x;
    }

    leds[x + (25*y)] = buff_col;
  }
  //Buff U
  for(int i=0; i<32; i++)
  {
    int x = buff_U[i][0] - 1;
    int y = 19 - (buff_U[i][1] - 1);

    if(y%2 == 1)
    {
      x = 24-x;
    }

    leds[x + (25*y)] = buff_col;
  }
  //Buff horn
  for(int i=0; i<6; i++)
  {
    int x = buff_horn[i][0] - 1;
    int y = 19 - (buff_horn[i][1] - 1);

    if(y%2 == 1)
    {
      x = 24-x;
    }

    leds[x + (25*y)] = buff_col;
  }
  col_start += 10;
}
void buff2()
{
  //Buff background
  for(int i=0; i<NUM_LEDS; i++)
  {
    leds[i] = CRGB(10, 10, 10);
  }

  //Buff outline
  int col = col_start;
  for(int i=0; i<70; i++)
  {
    leds[pt_finder(buff.outer[i][0], buff.outer[i][1], 1)] = CHSV( (col + (i*256/70)) % 256, 255, 255);
  }
  
  //Buff C
  for(int i=0; i<34; i++)
  {
    int x = buff_C[i][0] - 1;
    int y = 19 - (buff_C[i][1] - 1);

    if(y%2 == 1)
    {
      x = 24-x;
    }

    leds[x + (25*y)] = CHSV( (col + (i*256/34)) % 256, 255, 255);
  }
  //Buff U
  for(int i=0; i<32; i++)
  {
    int x = buff_U[i][0] - 1;
    int y = 19 - (buff_U[i][1] - 1);

    if(y%2 == 1)
    {
      x = 24-x;
    }

    leds[x + (25*y)] = CHSV( (col + (i*256/32)) % 256, 255, 255);
  }
  //Buff horn
  for(int i=0; i<6; i++)
  {
    int x = buff_horn[i][0] - 1;
    int y = 19 - (buff_horn[i][1] - 1);

    if(y%2 == 1)
    {
      x = 24-x;
    }

    leds[x + (25*y)] = CHSV( (col + (i*256/34)) % 256, 255, 255);
  }
  col_start += 10;
}
void buff2_muted()
{
  //Buff background
  for(int i=0; i<NUM_LEDS; i++)
  {
    leds[i] = CRGB(10, 10, 10);
  }

  //Buff outline
  int col = col_start;
  for(int i=0; i<70; i++)
  {
    int x = buff_outer[i][0] - 1;
    int y = 19 - (buff_outer[i][1] - 1);

    if(y%2 == 1)
    {
      x = 24-x;
    }

    leds[x + (25*y)] = CHSV( (col + (i*256/70)) % 256, 150, 255);
  }
  //Buff C
  for(int i=0; i<34; i++)
  {
    int x = buff_C[i][0] - 1;
    int y = 19 - (buff_C[i][1] - 1);

    if(y%2 == 1)
    {
      x = 24-x;
    }

    leds[x + (25*y)] = CHSV( (col + (i*256/34)) % 256, 150, 255);
  }
  //Buff U
  for(int i=0; i<32; i++)
  {
    int x = buff_U[i][0] - 1;
    int y = 19 - (buff_U[i][1] - 1);

    if(y%2 == 1)
    {
      x = 24-x;
    }

    leds[x + (25*y)] = CHSV( (col + (i*256/32)) % 256, 150, 255);
  }
  //Buff horn
  for(int i=0; i<6; i++)
  {
    int x = buff_horn[i][0] - 1;
    int y = 19 - (buff_horn[i][1] - 1);

    if(y%2 == 1)
    {
      x = 24-x;
    }

    leds[x + (25*y)] = CHSV( (col + (i*256/34)) % 256, 150, 255);
  }
  col_start += 10;
}
void buff3()
{
  //Buff background
  bpm6();

  //Buff outline
  for(int i=0; i<70; i++)
  {
    int x = buff_outer[i][0] - 1;
    int y = 19 - (buff_outer[i][1] - 1);

    if(y%2 == 1)
    {
      x = 24-x;
    }

    leds[x + (25*y)] = CRGB(255, 255, 255);
  }
  //Buff C
  for(int i=0; i<34; i++)
  {
    int x = buff_C[i][0] - 1;
    int y = 19 - (buff_C[i][1] - 1);

    if(y%2 == 1)
    {
      x = 24-x;
    }

    leds[x + (25*y)] = CRGB(255, 255, 255);
  }
  //Buff U
  for(int i=0; i<32; i++)
  {
    int x = buff_U[i][0] - 1;
    int y = 19 - (buff_U[i][1] - 1);

    if(y%2 == 1)
    {
      x = 24-x;
    }

    leds[x + (25*y)] = CRGB(255, 255, 255);
  }
  //Buff horn
  for(int i=0; i<6; i++)
  {
    int x = buff_horn[i][0] - 1;
    int y = 19 - (buff_horn[i][1] - 1);

    if(y%2 == 1)
    {
      x = 24-x;
    }

    leds[x + (25*y)] = CRGB(255, 255, 255);
  }
}

void wow()
{
  for(int i=0; i<NUM_LEDS; i++)
  {
    leds[i] = CRGB(random8(), random8(), random8());
  }
}
void wow_hype()
{
  for(int i=0; i<NUM_LEDS; i++)
  {
    leds[i] = CHSV(random8(), 255, 255);
  }
}
void wow2()
{
  CRGB col;
  col = CRGB(random8(), random8(), random8());
  for(int i=0; i<NUM_LEDS; i++)
  {
    leds[i] = col;
  }
}

int offset = 0;
void wow3()
{
  for(int i=0; i<NUM_LEDS; i++)
  {
      leds[i] = CRGB(i%255, (i + offset)%255, (i * offset)%255);
  }
  offset++;
}

void rainbow()
{
  // FastLED's built-in rainbow generator
  fill_rainbow( leds, NUM_LEDS, gHue, 7);
}

void rainbowWithGlitter()
{
  // built-in FastLED rainbow, plus some random sparkly glitter
  rainbow();
  addGlitter(80);
}

void addGlitter( fract8 chanceOfGlitter)
{
  if( random8() < chanceOfGlitter) {
    leds[ random16(NUM_LEDS) ] += CRGB::White;
  }
}

void confetti()
{
  // random colored speckles that blink in and fade smoothly
  fadeToBlackBy( leds, NUM_LEDS, 10);
  int pos = random16(NUM_LEDS);
  leds[pos] += CHSV( gHue + random8(64), 200, 255);
}

int val = 0;
void strobe()
{
  if(val == 0)
  {
    val = 1;
  }
  else
  {
    val = 0;
  }
  CRGB col = CRGB(255*val, 255*val, 255*val);
  for(int i=0; i<NUM_LEDS; i++)
  {
    leds[i] = col;
  }
}

void sinelon()
{
  // a colored dot sweeping back and forth, with fading trails
  fadeToBlackBy( leds, NUM_LEDS, 20);
  int pos = beatsin16( 13, 0, NUM_LEDS-1 );
  leds[pos] += CHSV( gHue, 255, 192);
}
void sinelon2()
{
  // a colored dot sweeping back and forth, with fading trails
  fadeToBlackBy( leds, NUM_LEDS, 20);
  int pos = beatsin16( 13, 0, NUM_LEDS-1 );
  int pos2 = beatsin16( 13, 0, NUM_LEDS-1, 5 );
  int pos3 = beatsin16( 13, 0, NUM_LEDS-1, 10 );
  int pos4 = beatsin16( 13, 0, NUM_LEDS-1, 15 );
  int pos5 = beatsin16( 13, 0, NUM_LEDS-1, 20 );
  int pos6 = beatsin16( 13, 0, NUM_LEDS-1, 25 );
  leds[pos] += CHSV( gHue, 255, 192);
  leds[pos2] += CHSV( gHue, 255, 192);
  leds[pos3] += CHSV( gHue, 255, 192);
  leds[pos4] += CHSV( gHue, 255, 192);
  leds[pos5] += CHSV( gHue, 255, 192);
  leds[pos6] += CHSV( gHue, 255, 192);
}

void bpm()
{
  // colored stripes pulsing at a defined Beats-Per-Minute (BPM)
  uint8_t BeatsPerMinute = 62;
  CRGBPalette16 palette = CloudColors_p;
  uint8_t beat = beatsin8( BeatsPerMinute, 64, 255);
  for( int i = 0; i < NUM_LEDS; i++) { //9948
    leds[i] = ColorFromPalette(palette, gHue+(i*2), beat-gHue+(i*10));
  }
}

void bpm2()
{
  // colored stripes pulsing at a defined Beats-Per-Minute (BPM)
  uint8_t BeatsPerMinute = 62;
  CRGBPalette16 palette = LavaColors_p;
  uint8_t beat = beatsin8( BeatsPerMinute, 64, 255);
  for( int i = 0; i < NUM_LEDS; i++) { //9948
    leds[i] = ColorFromPalette(palette, gHue+(i*2), beat-gHue+(i*10));
  }
}

void bpm3()
{
  // colored stripes pulsing at a defined Beats-Per-Minute (BPM)
  uint8_t BeatsPerMinute = 62;
  CRGBPalette16 palette = OceanColors_p;
  uint8_t beat = beatsin8( BeatsPerMinute, 64, 255);
  for( int i = 0; i < NUM_LEDS; i++) { //9948
    leds[i] = ColorFromPalette(palette, gHue+(i*2), beat-gHue+(i*10));
  }
}

void bpm4()
{
  // colored stripes pulsing at a defined Beats-Per-Minute (BPM)
  uint8_t BeatsPerMinute = 62;
  CRGBPalette16 palette = ForestColors_p;
  uint8_t beat = beatsin8( BeatsPerMinute, 64, 255);
  for( int i = 0; i < NUM_LEDS; i++) { //9948
    leds[i] = ColorFromPalette(palette, gHue+(i*2), beat-gHue+(i*10));
  }
}

void bpm5()
{
  // colored stripes pulsing at a defined Beats-Per-Minute (BPM)
  uint8_t BeatsPerMinute = 62;
  CRGBPalette16 palette = RainbowColors_p;
  uint8_t beat = beatsin8( BeatsPerMinute, 64, 255);
  for( int i = 0; i < NUM_LEDS; i++) { //9948
    leds[i] = ColorFromPalette(palette, gHue+(i*2), beat-gHue+(i*10));
  }
}

void bpm6()
{
  // colored stripes pulsing at a defined Beats-Per-Minute (BPM)
  uint8_t BeatsPerMinute = 62;
  CRGBPalette16 palette = RainbowStripeColors_p;
  uint8_t beat = beatsin8( BeatsPerMinute, 64, 255);
  for( int i = 0; i < NUM_LEDS; i++) { //9948
    leds[i] = ColorFromPalette(palette, gHue+(i*2), beat-gHue+(i*10));
  }
}

void bpm7()
{
  // colored stripes pulsing at a defined Beats-Per-Minute (BPM)
  uint8_t BeatsPerMinute = 62;
  CRGBPalette16 palette = PartyColors_p;
  uint8_t beat = beatsin8( BeatsPerMinute, 64, 255);
  for( int i = 0; i < NUM_LEDS; i++) { //9948
    leds[i] = ColorFromPalette(palette, gHue+(i*2), beat-gHue+(i*10));
  }
}

void bpm8()
{
  // colored stripes pulsing at a defined Beats-Per-Minute (BPM)
  uint8_t BeatsPerMinute = 62;
  CRGBPalette16 palette = HeatColors_p;
  uint8_t beat = beatsin8( BeatsPerMinute, 64, 255);
  for( int i = 0; i < NUM_LEDS; i++) { //9948
    leds[i] = ColorFromPalette(palette, gHue+(i*2), beat-gHue+(i*10));
  }
}

void juggle() {
  // eight colored dots, weaving in and out of sync with each other
  fadeToBlackBy( leds, NUM_LEDS, 20);
  byte dothue = 0;
  for( int i = 0; i < 8; i++) {
    leds[beatsin16( i+7, 0, NUM_LEDS-1 )] |= CHSV(dothue, 200, 255);
    dothue += 32;
  }
}
