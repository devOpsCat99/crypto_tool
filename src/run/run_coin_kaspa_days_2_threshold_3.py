from objects.simulator            import Simulator
from objects.crypto_configuration import cryptoConfiguration_bitvavo
from objects.model_configuration  import modelConfiguration

# Simulator configuration
file = "/mnt/c/Github/crypto_tool/files/kaspa/days_2/threshold_3/simulation.log"
startingMoney = 100

# Crypto configuration
coinName = "kaspa"
period   = '2' 

cryptoCnf = cryptoConfiguration_bitvavo(coinName, period)

# Model configuration
fitModel            = "fourier4"
minLocalDiff        = 0.75
thresholdAction     = 3
rollingWindowFactor = 5

modelCnf = modelConfiguration(fitModel, minLocalDiff, thresholdAction, rollingWindowFactor)

# Create simulator
simulator = Simulator(cryptoCnf, modelCnf, file, startingMoney, thresholdAction).run()
