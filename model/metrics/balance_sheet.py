from model.stock import MetricsMeta
from model.expr.crawl import Crawl


def metrics():
    metas = [
        # total_share	float	Y	期末总股本
        MetricsMeta("total_share", Crawl("total_share")),
        # cap_rese	float	Y	资本公积金
        MetricsMeta("cap_rese", Crawl("cap_rese")),
        # undistr_porfit	float	Y	未分配利润
        MetricsMeta("undistr_porfit", Crawl("undistr_porfit")),
        # surplus_rese	float	Y	盈余公积金
        MetricsMeta("surplus_rese", Crawl("surplus_rese")),
        # special_rese	float	Y	专项储备
        MetricsMeta("special_rese", Crawl("special_rese")),
        # money_cap	float	Y	货币资金
        MetricsMeta("money_cap", Crawl("money_cap")),
        # trad_asset	float	Y	交易性金融资产
        MetricsMeta("trad_asset", Crawl("trad_asset")),
        # notes_receiv	float	Y	应收票据
        MetricsMeta("notes_receiv", Crawl("notes_receiv")),
        # accounts_receiv	float	Y	应收账款
        MetricsMeta("accounts_receiv", Crawl("accounts_receiv")),
        # oth_receiv	float	Y	其他应收款
        MetricsMeta("oth_receiv", Crawl("oth_receiv")),
        # prepayment	float	Y	预付款项
        MetricsMeta("prepayment", Crawl("prepayment")),
        # div_receiv	float	Y	应收股利
        MetricsMeta("div_receiv", Crawl("div_receiv")),
        # int_receiv	float	Y	应收利息
        MetricsMeta("int_receiv", Crawl("int_receiv")),
        # inventories	float	Y	存货
        MetricsMeta("inventories", Crawl("inventories")),
        # amor_exp	float	Y	长期待摊费用
        MetricsMeta("amor_exp", Crawl("amor_exp")),
        # nca_within_1y	float	Y	一年内到期的非流动资产
        MetricsMeta("nca_within_1y", Crawl("nca_within_1y")),
        # sett_rsrv	float	Y	结算备付金
        MetricsMeta("sett_rsrv", Crawl("sett_rsrv")),
        # loanto_oth_bank_fi	float	Y	拆出资金
        MetricsMeta("loanto_oth_bank_fi", Crawl("loanto_oth_bank_fi")),
        # premium_receiv	float	Y	应收保费
        MetricsMeta("premium_receiv", Crawl("premium_receiv")),
        # reinsur_receiv	float	Y	应收分保账款
        MetricsMeta("reinsur_receiv", Crawl("reinsur_receiv")),
        # reinsur_res_receiv	float	Y	应收分保合同准备金
        MetricsMeta("reinsur_res_receiv", Crawl("reinsur_res_receiv")),
        # pur_resale_fa	float	Y	买入返售金融资产
        MetricsMeta("pur_resale_fa", Crawl("pur_resale_fa")),
        # oth_cur_assets	float	Y	其他流动资产
        MetricsMeta("oth_cur_assets", Crawl("oth_cur_assets")),
        # total_cur_assets	float	Y	流动资产合计
        MetricsMeta("total_cur_assets", Crawl("total_cur_assets")),
        # fa_avail_for_sale	float	Y	可供出售金融资产
        MetricsMeta("fa_avail_for_sale", Crawl("fa_avail_for_sale")),
        # htm_invest	float	Y	持有至到期投资
        MetricsMeta("htm_invest", Crawl("htm_invest")),
        # lt_eqt_invest	float	Y	长期股权投资
        MetricsMeta("lt_eqt_invest", Crawl("lt_eqt_invest")),
        # invest_real_estate	float	Y	投资性房地产
        MetricsMeta("invest_real_estate", Crawl("invest_real_estate")),
        # time_deposits	float	Y	定期存款
        MetricsMeta("time_deposits", Crawl("time_deposits")),
        # oth_assets	float	Y	其他资产
        MetricsMeta("oth_assets", Crawl("oth_assets")),
        # lt_rec	float	Y	长期应收款
        MetricsMeta("lt_rec", Crawl("lt_rec")),
        # fix_assets	float	Y	固定资产
        MetricsMeta("fix_assets", Crawl("fix_assets")),
        # cip	float	Y	在建工程
        MetricsMeta("cip", Crawl("cip")),
        # const_materials	float	Y	工程物资
        MetricsMeta("const_materials", Crawl("const_materials")),
        # fixed_assets_disp	float	Y	固定资产清理
        MetricsMeta("fixed_assets_disp", Crawl("fixed_assets_disp")),
        # produc_bio_assets	float	Y	生产性生物资产
        MetricsMeta("produc_bio_assets", Crawl("produc_bio_assets")),
        # oil_and_gas_assets	float	Y	油气资产
        MetricsMeta("oil_and_gas_assets", Crawl("oil_and_gas_assets")),
        # intan_assets	float	Y	无形资产
        MetricsMeta("intan_assets", Crawl("intan_assets")),
        # r_and_d	float	Y	研发支出
        MetricsMeta("r_and_d", Crawl("r_and_d")),
        # goodwill	float	Y	商誉
        MetricsMeta("goodwill", Crawl("goodwill")),
        # lt_amor_exp	float	Y	长期待摊费用
        MetricsMeta("lt_amor_exp", Crawl("lt_amor_exp")),
        # defer_tax_assets	float	Y	递延所得税资产
        MetricsMeta("defer_tax_assets", Crawl("defer_tax_assets")),
        # decr_in_disbur	float	Y	发放贷款及垫款
        MetricsMeta("decr_in_disbur", Crawl("decr_in_disbur")),
        # oth_nca	float	Y	其他非流动资产
        MetricsMeta("oth_nca", Crawl("oth_nca")),
        # total_nca	float	Y	非流动资产合计
        MetricsMeta("total_nca", Crawl("total_nca")),
        # cash_reser_cb	float	Y	现金及存放中央银行款项
        MetricsMeta("cash_reser_cb", Crawl("cash_reser_cb")),
        # depos_in_oth_bfi	float	Y	存放同业和其它金融机构款项
        MetricsMeta("depos_in_oth_bfi", Crawl("depos_in_oth_bfi")),
        # prec_metals	float	Y	贵金属
        MetricsMeta("prec_metals", Crawl("prec_metals")),
        # deriv_assets	float	Y	衍生金融资产
        MetricsMeta("deriv_assets", Crawl("deriv_assets")),
        # rr_reins_une_prem	float	Y	应收分保未到期责任准备金
        MetricsMeta("rr_reins_une_prem", Crawl("rr_reins_une_prem")),
        # rr_reins_outstd_cla	float	Y	应收分保未决赔款准备金
        MetricsMeta("rr_reins_outstd_cla", Crawl("rr_reins_outstd_cla")),
        # rr_reins_lins_liab	float	Y	应收分保寿险责任准备金
        MetricsMeta("rr_reins_lins_liab", Crawl("rr_reins_lins_liab")),
        # rr_reins_lthins_liab	float	Y	应收分保长期健康险责任准备金
        MetricsMeta("rr_reins_lthins_liab", Crawl("rr_reins_lthins_liab")),
        # refund_depos	float	Y	存出保证金
        MetricsMeta("refund_depos", Crawl("refund_depos")),
        # ph_pledge_loans	float	Y	保户质押贷款
        MetricsMeta("ph_pledge_loans", Crawl("ph_pledge_loans")),
        # refund_cap_depos	float	Y	存出资本保证金
        MetricsMeta("refund_cap_depos", Crawl("refund_cap_depos")),
        # indep_acct_assets	float	Y	独立账户资产
        MetricsMeta("indep_acct_assets", Crawl("indep_acct_assets")),
        # client_depos	float	Y	其中：客户资金存款
        MetricsMeta("client_depos", Crawl("client_depos")),
        # client_prov	float	Y	其中：客户备付金
        MetricsMeta("client_prov", Crawl("client_prov")),
        # transac_seat_fee	float	Y	其中:交易席位费
        MetricsMeta("transac_seat_fee", Crawl("transac_seat_fee")),
        # invest_as_receiv	float	Y	应收款项类投资
        MetricsMeta("invest_as_receiv", Crawl("invest_as_receiv")),
        # total_assets	float	Y	资产总计
        MetricsMeta("total_assets", Crawl("total_assets")),
        # lt_borr	float	Y	长期借款
        MetricsMeta("lt_borr", Crawl("lt_borr")),
        # st_borr	float	Y	短期借款
        MetricsMeta("st_borr", Crawl("st_borr")),
        # cb_borr	float	Y	向中央银行借款
        MetricsMeta("cb_borr", Crawl("cb_borr")),
        # depos_ib_deposits	float	Y	吸收存款及同业存放
        MetricsMeta("depos_ib_deposits", Crawl("depos_ib_deposits")),
        # loan_oth_bank	float	Y	拆入资金
        MetricsMeta("loan_oth_bank", Crawl("loan_oth_bank")),
        # trading_fl	float	Y	交易性金融负债
        MetricsMeta("trading_fl", Crawl("trading_fl")),
        # notes_payable	float	Y	应付票据
        MetricsMeta("notes_payable", Crawl("notes_payable")),
        # acct_payable	float	Y	应付账款
        MetricsMeta("acct_payable", Crawl("acct_payable")),
        # adv_receipts	float	Y	预收款项
        MetricsMeta("adv_receipts", Crawl("adv_receipts")),
        # sold_for_repur_fa	float	Y	卖出回购金融资产款
        MetricsMeta("sold_for_repur_fa", Crawl("sold_for_repur_fa")),
        # comm_payable	float	Y	应付手续费及佣金
        MetricsMeta("comm_payable", Crawl("comm_payable")),
        # payroll_payable	float	Y	应付职工薪酬
        MetricsMeta("payroll_payable", Crawl("payroll_payable")),
        # taxes_payable	float	Y	应交税费
        MetricsMeta("taxes_payable", Crawl("taxes_payable")),
        # int_payable	float	Y	应付利息
        MetricsMeta("int_payable", Crawl("int_payable")),
        # div_payable	float	Y	应付股利
        MetricsMeta("div_payable", Crawl("div_payable")),
        # oth_payable	float	Y	其他应付款
        MetricsMeta("oth_payable", Crawl("oth_payable")),
        # acc_exp	float	Y	预提费用
        MetricsMeta("acc_exp", Crawl("acc_exp")),
        # deferred_inc	float	Y	递延收益
        MetricsMeta("deferred_inc", Crawl("deferred_inc")),
        # st_bonds_payable	float	Y	应付短期债券
        MetricsMeta("st_bonds_payable", Crawl("st_bonds_payable")),
        # payable_to_reinsurer	float	Y	应付分保账款
        MetricsMeta("payable_to_reinsurer", Crawl("payable_to_reinsurer")),
        # rsrv_insur_cont	float	Y	保险合同准备金
        MetricsMeta("rsrv_insur_cont", Crawl("rsrv_insur_cont")),
        # acting_trading_sec	float	Y	代理买卖证券款
        MetricsMeta("acting_trading_sec", Crawl("acting_trading_sec")),
        # acting_uw_sec	float	Y	代理承销证券款
        MetricsMeta("acting_uw_sec", Crawl("acting_uw_sec")),
        # non_cur_liab_due_1y	float	Y	一年内到期的非流动负债
        MetricsMeta("non_cur_liab_due_1y", Crawl("non_cur_liab_due_1y")),
        # oth_cur_liab	float	Y	其他流动负债
        MetricsMeta("oth_cur_liab", Crawl("oth_cur_liab")),
        # total_cur_liab	float	Y	流动负债合计
        MetricsMeta("total_cur_liab", Crawl("total_cur_liab")),
        # bond_payable	float	Y	应付债券
        MetricsMeta("bond_payable", Crawl("bond_payable")),
        # lt_payable	float	Y	长期应付款
        MetricsMeta("lt_payable", Crawl("lt_payable")),
        # specific_payables	float	Y	专项应付款
        MetricsMeta("specific_payables", Crawl("specific_payables")),
        # estimated_liab	float	Y	预计负债
        MetricsMeta("estimated_liab", Crawl("estimated_liab")),
        # defer_tax_liab	float	Y	递延所得税负债
        MetricsMeta("defer_tax_liab", Crawl("defer_tax_liab")),
        # defer_inc_non_cur_liab	float	Y	递延收益-非流动负债
        MetricsMeta("defer_inc_non_cur_liab",
                      Crawl("defer_inc_non_cur_liab")),
        # oth_ncl	float	Y	其他非流动负债
        MetricsMeta("oth_ncl", Crawl("oth_ncl")),
        # total_ncl	float	Y	非流动负债合计
        MetricsMeta("total_ncl", Crawl("total_ncl")),
        # depos_oth_bfi	float	Y	同业和其它金融机构存放款项
        MetricsMeta("depos_oth_bfi", Crawl("depos_oth_bfi")),
        # deriv_liab	float	Y	衍生金融负债
        MetricsMeta("deriv_liab", Crawl("deriv_liab")),
        # depos	float	Y	吸收存款
        MetricsMeta("depos", Crawl("depos")),
        # agency_bus_liab	float	Y	代理业务负债
        MetricsMeta("agency_bus_liab", Crawl("agency_bus_liab")),
        # oth_liab	float	Y	其他负债
        MetricsMeta("defer_tax_liab", Crawl("defer_tax_liab")),
        # prem_receiv_adva	float	Y	预收保费
        MetricsMeta("prem_receiv_adva", Crawl("prem_receiv_adva")),
        # depos_received	float	Y	存入保证金
        MetricsMeta("depos_received", Crawl("depos_received")),
        # ph_invest	float	Y	保户储金及投资款
        MetricsMeta("ph_invest", Crawl("ph_invest")),
        # reser_une_prem	float	Y	未到期责任准备金
        MetricsMeta("reser_une_prem", Crawl("reser_une_prem")),
        # reser_outstd_claims	float	Y	未决赔款准备金
        MetricsMeta("reser_outstd_claims", Crawl("reser_outstd_claims")),
        # reser_lins_liab	float	Y	寿险责任准备金
        MetricsMeta("reser_lins_liab", Crawl("reser_lins_liab")),
        # reser_lthins_liab	float	Y	长期健康险责任准备金
        MetricsMeta("reser_lthins_liab", Crawl("reser_lthins_liab")),
        # indept_acc_liab	float	Y	独立账户负债
        MetricsMeta("indept_acc_liab", Crawl("indept_acc_liab")),
        # pledge_borr	float	Y	其中:质押借款
        MetricsMeta("pledge_borr", Crawl("pledge_borr")),
        # indem_payable	float	Y	应付赔付款
        MetricsMeta("indem_payable", Crawl("indem_payable")),
        # policy_div_payable	float	Y	应付保单红利
        MetricsMeta("policy_div_payable", Crawl("policy_div_payable")),
        # total_liab	float	Y	负债合计
        MetricsMeta("total_liab", Crawl("total_liab")),
        # treasury_share	float	Y	减:库存股
        MetricsMeta("treasury_share", Crawl("treasury_share")),
        # ordin_risk_reser	float	Y	一般风险准备
        MetricsMeta("ordin_risk_reser", Crawl("ordin_risk_reser")),
        # forex_differ	float	Y	外币报表折算差额
        MetricsMeta("forex_differ", Crawl("forex_differ")),
        # invest_loss_unconf	float	Y	未确认的投资损失
        MetricsMeta("invest_loss_unconf", Crawl("invest_loss_unconf")),
        # minority_int	float	Y	少数股东权益
        MetricsMeta("minority_int", Crawl("deferminority_int_tax_liab")),
        # total_hldr_eqy_exc_min_int	float	Y	股东权益合计(不含少数股东权益)
        MetricsMeta("total_hldr_eqy_exc_min_int",
                      Crawl("total_hldr_eqy_exc_min_int")),
        # total_hldr_eqy_inc_min_int	float	Y	股东权益合计(含少数股东权益)
        MetricsMeta("total_hldr_eqy_inc_min_int",
                      Crawl("total_hldr_eqy_inc_min_int")),
        # total_liab_hldr_eqy	float	Y	负债及股东权益总计
        MetricsMeta("total_liab_hldr_eqy", Crawl("total_liab_hldr_eqy")),
        # lt_payroll_payable	float	Y	长期应付职工薪酬
        MetricsMeta("lt_payroll_payable", Crawl("lt_payroll_payable")),
        # oth_comp_income	float	Y	其他综合收益
        MetricsMeta("oth_comp_income", Crawl("oth_comp_income")),
        # oth_eqt_tools	float	Y	其他权益工具
        MetricsMeta("oth_eqt_tools", Crawl("oth_eqt_tools")),
        # oth_eqt_tools_p_shr	float	Y	其他权益工具(优先股)
        MetricsMeta("oth_eqt_tools_p_shr", Crawl("oth_eqt_tools_p_shr")),
        # lending_funds	float	Y	融出资金
        MetricsMeta("lending_funds", Crawl("lending_funds")),
        # acc_receivable	float	Y	应收款项
        MetricsMeta("acc_receivable", Crawl("acc_receivable")),
        # st_fin_payable	float	Y	应付短期融资款
        MetricsMeta("st_fin_payable", Crawl("st_fin_payable")),
        # payables	float	Y	应付款项
        MetricsMeta("payables", Crawl("payables")),
        # hfs_assets	float	Y	持有待售的资产
        MetricsMeta("hfs_assets", Crawl("hfs_assets")),
        # hfs_sales	float	Y	持有待售的负债
        MetricsMeta("hfs_sales", Crawl("hfs_sales"))
    ]
    return metas
