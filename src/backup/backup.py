# # FFT para estimar coeficientes iniciales
# fft_coeffs = np.fft.fft(y_data) / len(y_data)
# a0_init = np.mean(y_data)  # MATLAB usa la media como a0
# a1_init, a2_init, a3_init, a4_init = 2 * np.real(fft_coeffs[1:5])
# b1_init, b2_init, b3_init, b4_init = -2 * np.imag(fft_coeffs[1:5])

# # Estimar p_value inicial como MATLAB
# p_init = 2 * np.pi / (np.max(xdata_norm) - np.min(xdata_norm))

# # Valores iniciales
# p0 = [a0_init, a1_init, b1_init, a2_init, b2_init, a3_init, b3_init, a4_init, b4_init, p_init]

# figure, ax = plt.subplots(figsize=(8, 8))
# ax.plot(self.__times, self.__prices, label=f"Price [{self.__cryptoCnf.get_currency()}]", color='blue', linewidth = 1)
# ax.plot(self.__times, self.__fittedPrices, color='red', linewidth = 4)
# ax.plot(np.array([self.__times[self.__trendReference.get_refIdx()],self.__times[self.__trendReference.get_refIdx()]]), np.array([np.min(self.__prices), np.max(self.__prices)]), '--', color=[0.7, 0.7, 0.7], linewidth=1)
# ax.plot(self.__times,np.ones(len(self.__times)) * self.__trendReference.get_refPrice(), '--', color=[0.7, 0.7, 0.7], linewidth = 1)
# ax.plot(self.__times[self.__trendReference.get_refIdx()], self.__trendReference.get_refPrice(), 'o', color='black', markersize = 6)
# ax.plot(self.__times[self.__trendReference.get_refIdx():], functions.fit_data(self.__timesDecYear[self.__trendReference.get_refIdx():], self.__fittedPrices[self.__trendReference.get_refIdx():], np.ones(2), "lineal"), '-', color = 'black', linewidth = 4)   
# ax.set_facecolor('w')
# ax.set_xlim([min(self.__times), max(self.__times)])
# ax.set_ylim([min(self.__prices), max(self.__prices)])
# ax.set_title(self.__name)
# ax.text(self.__times.values[-1], self.__prices[-1], f"{(self.__trendReference.get_refImprovement()):.2f} %", fontweight='bold')
# figure.savefig("grafico2.png", format="png", dpi=500)
# plt.show()