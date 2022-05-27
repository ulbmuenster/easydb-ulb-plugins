[![Contributors][contributors-shield]][contributors-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

[contributors-shield]: https://img.shields.io/github/contributors/ulbmuenster/easydb-ulb-plugins.svg?style=flat-square
[contributors-url]: https://github.com/ulbmuenster/easydb-ulb-plugins/graphs/contributors
[issues-shield]: https://img.shields.io/github/issues/ulbmuenster/easydb-ulb-plugins.svg?style=flat-square
[issues-url]: https://github.com/ulbmuenster/easydb-ulb-plugins/issues
[license-shield]: https://img.shields.io/github/license/ulbmuenster/easydb-ulb-plugins.svg?style=flat-square
[license-url]: https://github.com/ulbmuenster/easydb-ulb-plugins/blob/master/LICENSE.txt

<br />
<p align="center">
  <a href="https://ulb.uni-muenster.de">
    <img src="https://www.uni-muenster.de/imperia/md/images/ulb2/_v/logo.svg" alt="Logo">
  </a>

  <h3 align="center">Plugins for easyDB</h3>
  <p align="center">
    <br />
    This plugin will convert formulas.
    <br />
    <br />
    <a href="https://ulb.uni-muenster.de">Visit ULB</a>
    ·
    <a href="https://www.programmfabrik.de/easydb/">Visit easyDB</a>
  </p>
</p>


## Getting Started

### Prerequisites

* easyDB Instance (with root Privileges)
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

Update an object that has "Mineralogie" and a "formel" field.

## Logging

Logs can be read via `sudo docker logs easydb-server` depending on the server.

## Contributing

Contributions are what make the open source community such an amazing place to be, learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## License

See `LICENSE` for more information.
