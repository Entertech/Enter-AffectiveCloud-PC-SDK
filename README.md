# Enter Affective Cloud SDK For PC

## Introduction

Enter Affective Cloud SDK For PC is provided by [Enter Technology](https://www.entertech.cn/), designed to work with Enter Technology's Bluetooth chip and the Affective Cloud platform. This SDK is developed in Python and can run on macOS, Linux, and Windows.

## Installation

`pip install affectivecloud`

## Features

1. Access Bluetooth data ([enterble](https://github.com/Entertech/Enter-Biomodule-BLE-PC-SDK))
2. Connect to the Affective Cloud server
3. Call the Affective Computing service
4. Receive data from the Affective Computing service

## Usage

See [examples](https://github.com/Entertech/Enter-AffectiveCloud-PC-SDK/tree/main/examples)

- [simple](https://github.com/Entertech/Enter-AffectiveCloud-PC-SDK/tree/main/examples/simple.py)
- [headband Demo](https://github.com/Entertech/Enter-AffectiveCloud-PC-SDK/tree/main/examples/headband_relatime_demo.py)
- [headband Demo GUI Version](https://github.com/Entertech/Enter-AffectiveCloud-PC-SDK/tree/main/examples/headband_relatime_gui_demo.py)

### Note

#### Device-related

Each type of device has a different name. When using the demo, please use the corresponding name or do not specify a name. If no name is specified, all devices under the same UUID will be enumerated.

#### Development Environment

The SDK by default supports Python runtime environments of version >= 3.6 and < 3.10; if you need to use versions above 3.10, please upgrade the websockets dependency package to version >= 10.0.

#### Environment Variables

When using the demo, you need to set the environment variables:

`APP_KEY`

`APP_SECRET`

`CLIENT_ID`

For details, refer to: [Authenticate and create a session](https://docs.affectivecloud.cn/%F0%9F%8E%99%E6%8E%A5%E5%8F%A3%E5%8D%8F%E8%AE%AE/%E4%BC%9A%E8%AF%9D%E5%8D%8F%E8%AE%AE#%E8%AE%A4%E8%AF%81%E5%B9%B6%E5%88%9B%E5%BB%BA%E5%AF%B9%E8%AF%9D%E7%9A%84-request)
