#!/usr/bin/env python3

import json

chip_103vf = json.load(open("data/chips/STM32F103VF.json"))
fsmc = [p for p in chip_103vf['cores'][0]['peripherals'] if p['name'] == 'FSMC'][0]

chip = json.load(open("data/chips/STM32F107RC.json"))
chip['cores'][0]['peripherals'].append(fsmc)
chip

json.dump(chip, open("data/chips/GD32F307VE.json", 'w'), indent=4)
