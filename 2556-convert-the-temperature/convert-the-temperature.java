class Solution {
    public double[] convertTemperature(double celsius) {
        double[] answer = new double[2];
        double kelvin;
        double fahrenheit;
        kelvin = celsius + 273.15;
        fahrenheit = (celsius * 1.80) + 32.00;
        answer[0] = kelvin;
        answer[1] = fahrenheit;
        return answer;
    }
}