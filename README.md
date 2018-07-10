# Vision for Blind

## Introduction

When a button is pushed or when the touchscreen is touched, the current image is captured from the
camera. The image is then converted and piped into a TensorFlow Lite classifier model that
identifies what is in the image. Up to three results with the highest confidence returned by the
classifier are shown on the screen, if there is an attached display. Also, the result is spoken out
loud using Text-To-Speech to the default audio output.


## Schematics

![Schematics](rpi3_schematics_tf.png)


## How to train your ~~Dragon 🐉~~ Model?

First thought after cloning this is that how can I train my own custom model, so that I can extend categories and all.


## Demo


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

## License

This is Float32 extension of [Google's Sample Image Classifier for Android](https://github.com/androidthings/sample-tensorflow-imageclassifier)

## Contributors

<details>
	<summary>Team Vision</summary>
		<ul>
		    <li><a href="https://github.com/prithaupadhyay">Pritha Upadhyay</a></li>
			<li><a href="https://github.com/VaaibhaviSingh">Vaaibhavi Singh</a></li>
			<li><a href="https://github.com/anshumanv">Anshuman Verma</a></li>
			<li><a href="https://github.com/aashutoshrathi">Aashutosh Rathi</a></li>
		</ul>
</details>
