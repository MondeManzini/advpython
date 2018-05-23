from abc import ABCMeta

class AbstractXpay: 
	__metaclass__ = ABCMeta
        @abstractmethod
	getCreditCardNo(self):pass
        @abstractmethod
	getCustomerName(self):pass
        @abstractmethod
	getCardExpMonth(self):pass
        @abstractmethod
	getCardExpYear(self):pass
        @abstractmethod
	getCardCVVNo(self):pass
        @abstractmethod
	getAmount(self):pass
	
        @abstractmethod
	setCreditCardNo(creditCardNo):pass
        @abstractmethod
	setCustomerName(customerName):pass
        @abstractmethod
	setCardExpMonth(cardExpMonth):pass
        @abstractmethod
	setCardExpYear(cardExpYear):pass
        @abstractmethod
	setCardCVVNo(cardCVVNo):pass
        @abstractmethod
	setAmount(amount):pass
	

class AbstractPayD:
	__metaclass__ = ABCMeta
        @abstractmethod
	getCustCardNo(self):pass
        @abstractmethod
	getCardOwnerName(self):pass
        @abstractmethod
	getCardExpMonthDate(self):pass
        @abstractmethod
	getCVVNo(self):pass
        @abstractmethod
	getTotalAmount(self):pass
	
        @abstractmethod
	setCustCardNo(custCardNo):pass
        @abstractmethod
	setCardOwnerName(cardOwnerName):pass
        @abstractmethod
	setCardExpMonthDate(cardExpMonthDate):pass
        @abstractmethod
	setCVVNo(cVVNo):pass
        @abstractmethod
	setTotalAmount(totalAmount):pass


class XpayToPayDAdapter(object,AbstractPayD):
	
	xpay;
	
	def __init__(self,xpay):
		self.xpay = xpay;
		setProp(self);
	        self.custCardNo;
	        self.cardOwnerName;
	        self.cardExpMonthDate;
	        self.cVVNo;
	        self.totalAmount;

	@Override
	public String getCustCardNo(self) :
		return custCardNo;

	@Override
	public String getCardOwnerName(self) :
		return cardOwnerName;

	@Override
	public String getCardExpMonthDate(self) :
		return cardExpMonthDate;

	@Override
	public Integer getCVVNo(self) :
		return cVVNo;

	@Override
	public Double getTotalAmount(self) :
		return totalAmount;

	@Override
	public void setCustCardNo(String custCardNo) :
		self.custCardNo = custCardNo;
	

	@Override
	public void setCardOwnerName(String cardOwnerName) :
		self.cardOwnerName = cardOwnerName;
	

	@Override
	public void setCardExpMonthDate(String cardExpMonthDate) :
		self.cardExpMonthDate = cardExpMonthDate;
	

	@Override
	public void setCVVNo(Integer cVVNo) :
		self.cVVNo = cVVNo;
	

	@Override
	public void setTotalAmount(Double totalAmount) :
		self.totalAmount = totalAmount;
	
	
	private void setProp(self):
		setCardOwnerName(self.xpay.getCustomerName(self));
		setCustCardNo(self.xpay.getCreditCardNo(self));
		setCardExpMonthDate(self.xpay.getCardExpMonth(self)+"/"+self.xpay.getCardExpYear());
		setCVVNo(self.xpay.getCardCVVNo(self).intValue());
		setTotalAmount(self.xpay.getAmount(self));
	


public class XpayImpl implements Xpay:

	private String creditCardNo;
	private String customerName;
	private String cardExpMonth;
	private String cardExpYear;
	private Short cardCVVNo;
	private Double amount;
	
	@Override
	public String getCreditCardNo(self) :
		return creditCardNo;
	

	@Override
	public String getCustomerName(self) :
		return customerName;
	

	@Override
	public String getCardExpMonth(self) :
		return cardExpMonth;
	

	@Override
	public String getCardExpYear(self) :
		return cardExpYear;
	

	@Override
	public Short getCardCVVNo(self) :
		return cardCVVNo;
	

	@Override
	public Double getAmount(self) :
		return amount;
	

	@Override
	public void setCreditCardNo(String creditCardNo) :
		self.creditCardNo = creditCardNo;
	

	@Override
	public void setCustomerName(String customerName) :
		self.customerName = customerName;
	

	@Override
	public void setCardExpMonth(String cardExpMonth) :
		self.cardExpMonth = cardExpMonth;
	

	@Override
	public void setCardExpYear(String cardExpYear) :
		self.cardExpYear = cardExpYear;
	

	@Override
	public void setCardCVVNo(Short cardCVVNo) :
		self.cardCVVNo = cardCVVNo;
	

	@Override
	public void setAmount(Double amount) :
		self.amount = amount;
	



if __name__ == '__main__':
	public static void main(String[] args) :
		
		// Object for Xpay
		Xpay xpay = XpayImpl();
		xpay.setCreditCardNo("4789565874102365");
		xpay.setCustomerName("Max Warner");
		xpay.setCardExpMonth("09");
		xpay.setCardExpYear("25");
		xpay.setCardCVVNo((short)235);
		xpay.setAmount(2565.23);
		
		PayD payD = new XpayToPayDAdapter(xpay);
		testPayD(payD);
	
	
	private static void testPayD(PayD payD):
		
		System.out.println(payD.getCardOwnerName(self));
		System.out.println(payD.getCustCardNo(self));
		System.out.println(payD.getCardExpMonthDate(self));
		System.out.println(payD.getCVVNo(self));
		System.out.println(payD.getTotalAmount(self));
	


