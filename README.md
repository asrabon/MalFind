# MalFind
CLI tool to search for a malware sample on various online sandboxes and malware repositories.

---

## Installation/First Time Run
1. Clone the repository
2. pip install -r requirements.txt
3. Rename your config.ini.example file to config.ini
4. Modify each source you want to use in the config.ini.example file to your corresponding API key, username, or password
5. (Optional) Test all sources by running "pytest test.py"
6. python malfind.py --hash [MD5, SHA1, SHA256]

---

## Currently Supported Sources/Repositories
* [Hybrid Analysis](https://www.hybrid-analysis.com/)
* [MalQuarium](https://malquarium.org/)
* [MalShare](https://malshare.com/)
* [Malware Bazaar](https://bazaar.abuse.ch/)
* [PolySwarm](https://polyswarm.io/)
* [Hatching Triage](https://tria.ge/dashboard)
* [URLhaus](https://urlhaus.abuse.ch/browse/)
* [VirusBay](https://beta.virusbay.io/)
* [VirusShare](https://virusshare.com/)

## Future Work
* Automated searching of [Any.run](https://app.any.run/)
