// Pricing
import Currency from './3-currency';

export default class Pricing {
  constructor(amount = '', currency) {
    this.amount = amount;
    this.currency = currency;
  }

displayFullPrice() {
  const code = (this.currency_code);
  const name = (this.currency._name);
  const money = `${this.amount} ${name} (${code})`;

  return money;
}

  static convertPrice(amount = 0, conversionRate = 0) {
    if (typeof amount !== 'number') {
      throw new TypeError('amount must be a string');
    }
    
