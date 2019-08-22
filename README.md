[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]


<br />
<p align="center">
  <a href="https://ulb.uni-muenster.de">
    <img src="https://www.uni-muenster.de/imperia/md/images/ulb2/_v/logo.svg" alt="Logo">
  </a>

  <h3 align="center">Plugins for easyDB</h3>
  <p align="center">
    <br />
    This plugin will generate a random or specific formatted inventory number (invnr) with help of an external service.
    It is developed by ULB Münster and Verbundzentrale des GBV (VZG) Göttingen.
    <br />
    <a href="https://ulb.uni-muenster.de">Visit ULB</a>
    ·
    <a href="https://www.gbv.de">Visit GBV</a>
    ·
    <a href="https://www.programmfabrik.de/easydb/">Visit easyDB</a>
  </p>
</p>


## Getting Started

### Prerequisites

* easyDB Instance (with root Privileges)
* [InvNr Service Instance](https://github.com/ulbmuenster/inventarnummer_service)
* Proper configured firewall / proxy

### Installation

1. Update your easydb5-master.yml

        extension:
            plugins:
            - name: ulb
                file: plugin/ulb/ulb.yml
        plugins:
            enabled+:
            - extension.ulb

2. Copy ulb.py and ulb.yml into `srv/easydb/config/plugin/ulb`
3. Restart easyDB Instance via `sudo /srv/easydb/maintain restart`

## Usage

Update a file with objecttype "ztest" and **leave field "invnr" blank**.
The Plugin will automatically insert a random invnr in this field when saving.

## Logging

Logs can be read via `sudo docker logs easydb-server`


## Roadmap

* Insert Configfile, so that other objecttypes can be handled
* Insert logic, such as, only certain number areas will be returned from the service
* Writing tests

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## License

Distributed under the MIT License. See `LICENSE` for more information.


## Contact

Dennis Voltz - [dennis.voltz@wwu.de](dennis.voltz@wwu.de)  

Adriano Neufend - [neufenda@wwu.de](neufenda@wwu.de)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=flat-square
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=flat-square
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=flat-square
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=flat-square
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=flat-square
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png