# FIN 439 Lab 13

## 1. S1-S10 Statement Classifications

- **S1 — Time-horizon and rebalancing constraint:** The reserve has a seven-year investment horizon and will be rebalanced annually.
- **S2 — Return objective:** The investment objective is to earn CPI + 4% annually, net of costs, over rolling five-year periods.
- **S3 — Liquidity constraint:** The foundation distributes $0.75 million each quarter and requires twelve months of distributions to be held in cash or daily-liquid government securities. For a $100 million reserve, the minimum required amount is $3 million, or 3% of the portfolio.
- **S4 — Benchmark:** Portfolio performance will be compared with a benchmark consisting of 60% global equities and 40% U.S. investment-grade bonds.
- **S5 — Investment constraint:** The portfolio must be long-only. Borrowing, short sales, and derivatives are prohibited.
- **S6 — Issuer-concentration constraint:** No single nonexempt issuer may represent more than 8% of the portfolio.
- **S7 — Turnover constraint:** Annual portfolio turnover cannot exceed 25% without committee approval.
- **S8 — Liquidity constraint:** At least 90% of the portfolio must be redeemable within five business days.
- **S9 — Risk constraint requiring clarification:** Unverifiable promise. The reserve cannot have a calendar-year loss greater than 10%, but the statement does not define the risk measure, how a breach will be determined, or what action will follow a breach. Therefore, it cannot be tested reliably as written.
- **S10 — Unspecified preferences and decision criterion:** Missing. No sector, ESG, tax, or home-bias preference has been stated. The CIO also has not identified what the pilot portfolio should optimize.

## 2. Portfolio D Evaluation

Portfolio D allocates 100% to cash and 0% to every other holding. It passes all five rules checked by `mandate.py`: its weights total 100%, its lowest weight is 0%, its reserve-eligible allocation is 100%, its five-day liquid allocation is 100%, and its largest nonexempt company exposure is 0%.

Despite passing every coded rule, Portfolio D could reasonably be rejected because of **S2**, the objective of earning CPI + 4% annually, net of costs, over rolling five-year periods. An all-cash portfolio is highly liquid, but it may not provide enough return to meet that objective. This does not prove that Portfolio D will fail S2; it shows that passing the compliance checks alone is not enough to establish that the portfolio is suitable.

## 3. One Question for the CIO

How should the 10% calendar-year loss limit in S9 be measured and monitored, and what action should be taken if the portfolio approaches or breaches that limit?

This clarification is necessary because S9 does not state whether the limit refers to realized losses, total portfolio return, a forecasted risk measure, or another calculation. It also does not specify a breach procedure.

## 4. Investment Policy Statement (IPS)

An Investment Policy Statement is a document that establishes an investor's objectives, investment restrictions, and guidelines for managing and evaluating a portfolio. The Meridian Foundation Reserve is a $100 million portfolio with a seven-year investment horizon and annual rebalancing. Its investment objective is to earn CPI + 4% annually, net of costs, over rolling five-year periods. Performance will be evaluated against a benchmark consisting of 60% global equities and 40% U.S. investment-grade bonds.

The foundation distributes $0.75 million quarterly. It must maintain twelve months of distributions, equal to $3 million or 3% of the portfolio, in cash or daily-liquid government securities. At least 90% of the portfolio must be redeemable within five business days.

The portfolio must be long-only and may not use borrowing, short sales, or derivatives. No single nonexempt issuer may exceed 8% of the portfolio. Annual portfolio turnover may not exceed 25% without committee approval.

The stated limit on calendar-year losses requires additional guidance concerning its measurement, monitoring, and breach procedure. The CIO must also clarify the pilot portfolio's decision criterion because no optimization objective or sector, ESG, tax, or home-bias preference has been specified.

## 5. Reflection

This exercise showed me that a portfolio can comply with every rule tested by a program without necessarily being appropriate for the client. The program can test clearly defined numerical requirements, such as liquidity and issuer concentration, but it cannot determine whether a portfolio is likely to achieve the return objective. Portfolio D demonstrates this limitation because an all-cash allocation passes every coded check while still raising a reasonable concern about the CPI + 4% objective.

I also learned that an investment mandate must use precise language before every statement can be converted into a compliance rule. S9 gives a 10% calendar-year loss limit, but it does not identify a risk measure or explain how a breach should be handled. An analyst should request clarification instead of inventing a test that may not reflect the CIO's intent.

## 6. Project 2 Client Mandate
Client: High-Net-Worth Individual (Fictional)
Client Background:
The client is a 45-year-old business executive with a $5 million investment portfolio. The client plans to retire at age 60 and wants to continue growing their wealth while maintaining financial stability and limiting exposure to significant market losses.
Investment Objective:
The client's primary objective is to achieve an average annual return of 7%, net of investment costs, over a 15-year investment horizon. The portfolio should balance long-term capital appreciation with wealth preservation while maintaining sufficient liquidity for unexpected financial needs.
Hard Constraints:
- The portfolio must be long-only, with no borrowing, short selling, or derivatives.
- No individual company may represent more than 8% of the portfolio. Diversified funds and U.S. Treasury securities are exempt.
- At least 25% of the portfolio must be invested in investment-grade bonds.
- At least 10% of the portfolio must be held in cash or highly liquid government securities.
- At least 90% of the portfolio must be redeemable within five business days.
- The portfolio will be rebalanced annually.
One Question for the Client:
What is the maximum annual portfolio loss you would be comfortable accepting while pursuing your 7% return objective?
The client's answer would help determine the appropriate allocation between equities, bonds, and cash. A lower tolerance for losses would require a more conservative investment strategy, while a higher tolerance could allow for greater equity exposure and potential long-term growth.
