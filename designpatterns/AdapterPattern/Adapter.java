package com.javacodegeeks.patterns.adapterpattern.xpay;

public interface Xpay {
	
	public String getCreditCardNo();
	public String getCustomerName();
	public String getCardExpMonth();
	public String getCardExpYear();
	public Short getCardCVVNo();
	public Double getAmount();
	
	public void setCreditCardNo(String creditCardNo);
	public void setCustomerName(String customerName);
	public void setCardExpMonth(String cardExpMonth);
	public void setCardExpYear(String cardExpYear);
	public void setCardCVVNo(Short cardCVVNo);
	public void setAmount(Double amount);
	
}
public interface PayD {
	
	public String getCustCardNo();
	public String getCardOwnerName();
	public String getCardExpMonthDate();
	public Integer getCVVNo();
	public Double getTotalAmount();
	
	public void setCustCardNo(String custCardNo);
	public void setCardOwnerName(String cardOwnerName);
	public void setCardExpMonthDate(String cardExpMonthDate);
	public void setCVVNo(Integer cVVNo);
	public void setTotalAmount(Double totalAmount);
}

public class XpayToPayDAdapter implements PayD{

	private String custCardNo;
	private String cardOwnerName;
	private String cardExpMonthDate;
	private Integer cVVNo;
	private Double totalAmount;
	
	private final Xpay xpay;
	
	public XpayToPayDAdapter(Xpay xpay){
		this.xpay = xpay;
		setProp();
	}

	@Override
	public String getCustCardNo() {
		return custCardNo;
	}

	@Override
	public String getCardOwnerName() {
		return cardOwnerName;
	}

	@Override
	public String getCardExpMonthDate() {
		return cardExpMonthDate;
	}

	@Override
	public Integer getCVVNo() {
		return cVVNo;
	}

	@Override
	public Double getTotalAmount() {
		return totalAmount;
	}

	@Override
	public void setCustCardNo(String custCardNo) {
		this.custCardNo = custCardNo;
	}

	@Override
	public void setCardOwnerName(String cardOwnerName) {
		this.cardOwnerName = cardOwnerName;
	}

	@Override
	public void setCardExpMonthDate(String cardExpMonthDate) {
		this.cardExpMonthDate = cardExpMonthDate;
	}

	@Override
	public void setCVVNo(Integer cVVNo) {
		this.cVVNo = cVVNo;
	}

	@Override
	public void setTotalAmount(Double totalAmount) {
		this.totalAmount = totalAmount;
	}
	
	private void setProp(){
		setCardOwnerName(this.xpay.getCustomerName());
		setCustCardNo(this.xpay.getCreditCardNo());
		setCardExpMonthDate(this.xpay.getCardExpMonth()+"/"+this.xpay.getCardExpYear());
		setCVVNo(this.xpay.getCardCVVNo().intValue());
		setTotalAmount(this.xpay.getAmount());
	}

}
public class XpayImpl implements Xpay{

	private String creditCardNo;
	private String customerName;
	private String cardExpMonth;
	private String cardExpYear;
	private Short cardCVVNo;
	private Double amount;
	
	@Override
	public String getCreditCardNo() {
		return creditCardNo;
	}

	@Override
	public String getCustomerName() {
		return customerName;
	}

	@Override
	public String getCardExpMonth() {
		return cardExpMonth;
	}

	@Override
	public String getCardExpYear() {
		return cardExpYear;
	}

	@Override
	public Short getCardCVVNo() {
		return cardCVVNo;
	}

	@Override
	public Double getAmount() {
		return amount;
	}

	@Override
	public void setCreditCardNo(String creditCardNo) {
		this.creditCardNo = creditCardNo;
	}

	@Override
	public void setCustomerName(String customerName) {
		this.customerName = customerName;
	}

	@Override
	public void setCardExpMonth(String cardExpMonth) {
		this.cardExpMonth = cardExpMonth;
	}

	@Override
	public void setCardExpYear(String cardExpYear) {
		this.cardExpYear = cardExpYear;
	}

	@Override
	public void setCardCVVNo(Short cardCVVNo) {
		this.cardCVVNo = cardCVVNo;
	}

	@Override
	public void setAmount(Double amount) {
		this.amount = amount;
	}

}

public class RunAdapterExample {

	public static void main(String[] args) {
		
		// Object for Xpay
		Xpay xpay = new XpayImpl();
		xpay.setCreditCardNo("4789565874102365");
		xpay.setCustomerName("Max Warner");
		xpay.setCardExpMonth("09");
		xpay.setCardExpYear("25");
		xpay.setCardCVVNo((short)235);
		xpay.setAmount(2565.23);
		
		PayD payD = new XpayToPayDAdapter(xpay);
		testPayD(payD);
	}
	
	private static void testPayD(PayD payD){
		
		System.out.println(payD.getCardOwnerName());
		System.out.println(payD.getCustCardNo());
		System.out.println(payD.getCardExpMonthDate());
		System.out.println(payD.getCVVNo());
		System.out.println(payD.getTotalAmount());
	}

}
