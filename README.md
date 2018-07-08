# Vision for Blind

## Introduction

When a button is pushed or when the touchscreen is touched, the current image is captured from the
camera. The image is then converted and piped into a TensorFlow Lite classifier model that
identifies what is in the image. Up to three results with the highest confidence returned by the
classifier are shown on the screen, if there is an attached display. Also, the result is spoken out
loud using Text-To-Speech to the default audio output.


## Screenshots

![TensorFlow Lite image classifier sample demo][demo-gif]


## Schematics

![Schematics](rpi3_schematics_tf.png)

## Run on Android Things Starter Kit

If you have an Android Things Starter Kit, you can easily run this sample on your i.MX7D development board from the [Android Things Toolkit](https://play.google.com/store/apps/details?id=com.google.android.things.companion&hl=en) app.

To run the sample on your i.MX7D development board:
  1. Set up your device using Toolkit
  2. Navigate to the Apps tab
  3. Select Run next to the Image Classifier sample.
  4. Press the "A" button on your Rainbow HAT or tap on the display to take a photo.

![Running Image Classifier Sample on Toolkit][toolkit-jpg]

## Enable auto-launch behavior

This sample app is currently configured to launch only when deployed from your
development machine. To enable the main activity to launch automatically on boot,
add the following `intent-filter` to the app's manifest file:

```xml
<activity ...>

   <intent-filter>
       <action android:name="android.intent.action.MAIN"/>
       <category android:name="android.intent.category.HOME"/>
       <category android:name="android.intent.category.DEFAULT"/>
   </intent-filter>

</activity>
```

