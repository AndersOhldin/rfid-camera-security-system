A small control system that is meant to depict a security system with an RFID-reader, camera logging (picture and date stored in MariaDB) and an unlocking mechanism. This is done through the use of 2 Raspberry Pis, a breadboard with a LED and a camera, and finally an RFID-reader.

Known flaws: the system locks itself for the duration of the unlocking of the door. This is due to this being a group project - I insisted on using a threaded approach in the server script, but it never got implemented.
