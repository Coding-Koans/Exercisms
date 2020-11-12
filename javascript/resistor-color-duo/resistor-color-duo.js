import { colorCode } from './../resistor-color/resistor-color'

export const decodedValue = (duo) => {
  const tensDigit = colorCode(duo[0]) * 10;
  const onesDigit = colorCode(duo[1]);
  return tensDigit + onesDigit;
};
