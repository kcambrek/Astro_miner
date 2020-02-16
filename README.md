# Astro_miner

This repository contains the Astro_miner class which can be used to mine the descriptions of the Nasa's Astronomy Picture of the Day (APOD) and all the descriptions from the start of APOD (June 16, 1995) till February 16, 2020)

To start mining, one first needs to obtain an API key from https://api.nasa.gov/ . This key can be passed to the mine method to start writing to a text file. To retrieve over 24 years of descriptions can take up to 8 hours. 

```
miner = Astro_miner.Astro_miner()

miner.mine(KEY)

```

I have used the date to fine tune a GTP-2 model to generate new astronomy descriptions. With some small changes to the class, the miner can also be used to get all the images over the last 24 years. This data could be of interest to develop GAN-networks.


Please note that the authorship of the descriptions is not mine, but belong the wonderful Robert Nemiroff and Jerry Bonnell who have written, coordinated, and edited APOD since 1995.


