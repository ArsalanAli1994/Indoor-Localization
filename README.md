# Indoor-Localization of Object Using Kalman Filter
This project involves incorporating an ESP32 or ESP8266 microcontroller, along with an Inertial Measurement Unit (IMU) sensor, into a robotic platform as part of an MRobotic Laboratory project. The IMU sensor provides data on the robot's orientation and movement in three-dimensional space.
Here's a brief overview of the project components and their functions:

ESP32 or ESP8266 Microcontroller: These are popular Wi-Fi and Bluetooth-enabled microcontrollers that serve as the main controller for the robotic platform. They are responsible for processing data from various sensors, communicating with the IMU sensor, and implementing the Kalman filter algorithm for real-time positioning estimation.


This project involves incorporating an ESP32 or ESP8266 microcontroller, along with an Inertial Measurement Unit (IMU) sensor, into a robotic platform as part of an MRobotic Laboratory project. The IMU sensor provides data on the robot's orientation and movement in three-dimensional space.

Here's a brief overview of the project components and their functions:

ESP32 or ESP8266 Microcontroller: These are popular Wi-Fi and Bluetooth-enabled microcontrollers that serve as the main controller for the robotic platform. They are responsible for processing data from various sensors, communicating with the IMU sensor, and implementing the Kalman filter algorithm for real-time positioning estimation.

IMU Sensor: The IMU sensor is used to measure the robot's orientation and motion. It typically consists of a gyroscope and accelerometer, which provide data about rotation rates and acceleration along three axes (X, Y, Z). Some IMU sensors may also include a magnetometer for measuring magnetic fields.

Kalman Filter Implementation: The Kalman filter is a mathematical algorithm used for estimating the state of a dynamic system based on noisy measurements over time. In this project, the Kalman filter takes data from the gyroscope and accelerometer of the IMU sensor to predict the position and orientation of the robot within an indoor environment. The filter integrates these sensor measurements along with any other available information (such as RSSI data from Wi-Fi signals) to improve the accuracy of the position estimation.

Wi-Fi RSSI Data: The Received Signal Strength Indication (RSSI) of Wi-Fi signals can be used as an additional input to the Kalman filter for localization purposes. By measuring the strength of Wi-Fi signals from known access points in the environment, the robot can estimate its distance from those access points and improve its position estimation.

Overall, this project aims to leverage sensor data from an IMU, along with Wi-Fi RSSI data, to implement a Kalman filter algorithm for real-time positioning estimation of a robotic platform within an indoor environment. The ESP32 or ESP8266 microcontroller serves as the central processing unit, coordinating sensor data acquisition, Kalman filtering, and control of the robotic platform.


<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<!-- [![CircleCI](https://circleci.com/gh/AlexeyAB/darknet.svg?style=svg)](https://circleci.com/gh/AlexeyAB/darknet)
[![License: Unlicense](https://img.shields.io/badge/license-Unlicense-blue.svg)](https://github.com/AlexeyAB/darknet/blob/master/LICENSE) -->


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <!-- <a href="https://ifttt.com/maker_webhooks">
    <img src="https://arduinodiy.files.wordpress.com/2018/01/webhookslogo.png" alt="Logo" width="80" height="80">
  </a> -->
  <h3 align="center">MRobotic Lab v1.0</h3>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The API</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <!-- <li><a href="#roadmap">Roadmap</a></li> -->
    <!-- <li><a href="#contributing">Contributing</a></li> -->
    <!-- <li><a href="#license">License</a></li> -->
    <li><a href="#contact">Contact</a></li>
    <!-- <li><a href="#acknowledgments">Acknowledgments</a></li> -->
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

This project implementation is the part of MRobotic Laboratory which contains the following workflow

* NodeMCU ESP8266 is embedded on the robotic vehicle to extract data from different sensors.
* Inertial Measurement Unit(IMU) connect via I2C with ESP8266 and RSSI is extract from ESP8266 with reference to Access Point. Where NodeMCU extract data with a specific sample rate and air the data over to Access point via TCP protocol.
* The provided Scripts 'RoboticDataTransfer3.py' gets data over the computational device and dumps the data in CSV file.
* Kalman Filter(KF_test.py) takes the data from the CSV file and predict the position of the Robotic Vehicle.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With
This section should list any major frameworks/libraries involved in the project.

* python3 - numpy
<!-- * [![https][https]][Https-url] -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<!-- GETTING STARTED -->
## Getting Started
This section provides the instruction how to setup the API on the system.

### Prerequisites

* python3

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._


1. Clone the repo
   ```bash
   git clone https://github.com/ArsalanAli400/Indoor-Localization.git
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage
Take the following steps to start the indoor predicts
1. Use the Python3 to run the script to get data from the robot.
   ```bash
   python3 RoboticDataTransfer3.py
   ```
2. Use Python3 to run script KF_test.py to robot postion
```bash
   python3 KF_test.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
<!-- ## Roadmap

- [x] Add Changelog
- [x] Add back to top links
- [ ] Add Additional Templates w/ Examples
- [ ] Add "components" document to easily copy & paste sections of the readme
- [ ] Multi-language Support
    - [ ] Chinese
    - [ ] Spanish

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- CONTRIBUTING -->
<!-- ## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request -->

<!-- <p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- LICENSE -->
<!-- ## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- CONTACT -->
## Contact

<!-- Your Name - [@your_twitter](https://twitter.com/a) - arsalan.ali.safeer@gmail.com -->

Project Link: [https://github.com/ArsalanAli400/Mroboticlab](https://github.com/ArsalanAli400/Mroboticlab.git)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
<!-- ## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
<!-- [contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555 -->
[linkedin-url]: https://www.linkedin.com/in/arsalan-ali-safeer-b618b41a8/
<!-- [product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com  -->
