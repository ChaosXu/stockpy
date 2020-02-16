from stockpy.metrics.base import MetricsMeta
from stockpy.expr import Crawl


def metrics():
    metas = [
        # net_profit	float	Y	净利润
        MetricsMeta('net_profit', Crawl(
            'cashflow', 'net_profit'), display='净利润'),
        # finan_exp	float	Y	财务费用
        MetricsMeta('finan_exp', Crawl(
            'cashflow', 'finan_exp'), display='财务费用'),
        # c_fr_sale_sg	float	Y	销售商品、提供劳务收到的现金
        MetricsMeta('c_fr_sale_sg', Crawl(
            'cashflow', 'c_fr_sale_sg'), display='销售商品、提供劳务收到的现金'),
        # recp_tax_rends	float	Y	收到的税费返还
        MetricsMeta('recp_tax_rends', Crawl(
            'cashflow', 'recp_tax_rends'), display='收到的税费返还'),
        # n_depos_incr_fi	float	Y	客户存款和同业存放款项净增加额
        MetricsMeta('n_depos_incr_fi', Crawl(
            'cashflow', 'n_depos_incr_fi'), display='客户存款和同业存放款项净增加额'),
        # n_incr_loans_cb	float	Y	向中央银行借款净增加额
        MetricsMeta('n_incr_loans_cb', Crawl(
            'cashflow', 'totaln_incr_loans_cb_share'), display='向中央银行借款净增加额'),
        # n_inc_borr_oth_fi	float	Y	向其他金融机构拆入资金净增加额
        MetricsMeta('n_inc_borr_oth_fi', Crawl(
            'cashflow', 'n_inc_borr_oth_fi'), display='向其他金融机构拆入资金净增加额'),
        # prem_fr_orig_contr	float	Y	收到原保险合同保费取得的现金
        MetricsMeta('prem_fr_orig_contr', Crawl(
            'cashflow', 'prem_fr_orig_contr'), display='收到原保险合同保费取得的现金'),
        # n_incr_insured_dep	float	Y	保户储金净增加额
        MetricsMeta('n_incr_insured_dep', Crawl(
            'cashflow', 'n_incr_insured_dep'), display='保户储金净增加额'),
        # n_reinsur_prem	float	Y	收到再保业务现金净额
        MetricsMeta('n_reinsur_prem', Crawl(
            'cashflow', 'n_reinsur_prem'), display='收到再保业务现金净额'),
        # n_incr_disp_tfa	float	Y	处置交易性金融资产净增加额
        MetricsMeta('n_incr_disp_tfa', Crawl(
            'cashflow', 'n_incr_disp_tfa'), display='处置交易性金融资产净增加额'),
        # ifc_cash_incr	float	Y	收取利息和手续费净增加额
        MetricsMeta('ifc_cash_incr', Crawl(
            'cashflow', 'ifc_cash_incr'), display='收取利息和手续费净增加额'),
        # n_incr_disp_faas	float	Y	处置可供出售金融资产净增加额
        MetricsMeta('n_incr_disp_faas', Crawl(
            'cashflow', 'n_incr_disp_faas'), display='处置可供出售金融资产净增加额'),
        # n_incr_loans_oth_bank	float	Y	拆入资金净增加额
        MetricsMeta('n_incr_loans_oth_bank', Crawl(
            'cashflow', 'n_incr_loans_oth_bank'), display='拆入资金净增加额'),
        # n_cap_incr_repur	float	Y	回购业务资金净增加额
        MetricsMeta('n_cap_incr_repur', Crawl(
            'cashflow', 'n_cap_incr_repur'), display='回购业务资金净增加额'),
        # c_fr_oth_operate_a	float	Y	收到其他与经营活动有关的现金
        MetricsMeta('c_fr_oth_operate_a', Crawl(
            'cashflow', 'c_fr_oth_operate_a'), display='收到其他与经营活动有关的现金'),
        # c_inf_fr_operate_a	float	Y	经营活动现金流入小计
        MetricsMeta('c_inf_fr_operate_a', Crawl(
            'cashflow', 'c_inf_fr_operate_a'), display='经营活动现金流入小计'),
        # c_paid_goods_s	float	Y	购买商品、接受劳务支付的现金
        MetricsMeta('c_paid_goods_s', Crawl(
            'cashflow', 'c_paid_goods_s'), display='购买商品、接受劳务支付的现金'),
        # c_paid_to_for_empl	float	Y	支付给职工以及为职工支付的现金
        MetricsMeta('c_paid_to_for_empl', Crawl(
            'cashflow', 'c_paid_to_for_empl'), display='支付给职工以及为职工支付的现金'),
        # c_paid_for_taxes	float	Y	支付的各项税费
        MetricsMeta('c_paid_for_taxes', Crawl(
            'cashflow', 'c_paid_for_taxes'), display='支付的各项税费'),
        # n_incr_clt_loan_adv	float	Y	客户贷款及垫款净增加额
        MetricsMeta('n_incr_clt_loan_adv', Crawl(
            'cashflow', 'n_incr_clt_loan_adv'), display='客户贷款及垫款净增加额'),
        # n_incr_dep_cbob	float	Y	存放央行和同业款项净增加额
        MetricsMeta('n_incr_dep_cbob', Crawl(
            'cashflow', 'n_incr_dep_cbob'), display='存放央行和同业款项净增加额'),
        # c_pay_claims_orig_inco	float	Y	支付原保险合同赔付款项的现金
        MetricsMeta('c_pay_claims_orig_inco',
                    Crawl('cashflow', 'c_pay_claims_orig_inco'),
                    display='支付原保险合同赔付款项的现金'),
        # pay_handling_chrg	float	Y	支付手续费的现金
        MetricsMeta('pay_handling_chrg', Crawl(
            'cashflow', 'pay_handling_chrg'), display='支付手续费的现金'),
        # pay_handling_chrg	float	Y	支付保单红利的现金
        MetricsMeta('pay_handling_chrg', Crawl(
            'cashflow', 'pay_handling_chrg'), display='支付保单红利的现金'),
        # oth_cash_pay_oper_act	float	Y	支付其他与经营活动有关的现金
        MetricsMeta('oth_cash_pay_oper_act', Crawl(
            'cashflow', 'oth_cash_pay_oper_act'), display='支付其他与经营活动有关的现金'),
        # st_cash_out_act	float	Y	经营活动现金流出小计
        MetricsMeta('st_cash_out_act', Crawl(
            'cashflow', 'st_cash_out_act'), display='经营活动现金流出小计'),
        # n_cashflow_act	float	Y	经营活动产生的现金流量净额
        MetricsMeta('n_cashflow_act', Crawl(
            'cashflow', 'n_cashflow_act'), display='经营现金流量净额'),
        # oth_recp_ral_inv_act	float	Y	收到其他与投资活动有关的现金
        MetricsMeta('oth_recp_ral_inv_act', Crawl(
            'cashflow', 'oth_recp_ral_inv_act'), display='收到其他与投资活动有关的现金'),
        # c_disp_withdrwl_invest	float	Y	收回投资收到的现金
        MetricsMeta('c_disp_withdrwl_invest',
                    Crawl('cashflow', 'c_disp_withdrwl_invest'),
                    display='收回投资收到的现金'),
        # c_recp_return_invest	float	Y	取得投资收益收到的现金
        MetricsMeta('c_recp_return_invest', Crawl(
            'cashflow', 'c_recp_return_invest'), display='取得投资收益收到的现金'),
        # n_recp_disp_fiolta	float	Y	处置固定资产、无形资产和其他长期资产收回的现金净额
        MetricsMeta('n_recp_disp_fiolta', Crawl(
            'cashflow', 'n_recp_disp_fiolta'),
            display='处置固定资产、无形资产和其他长期资产收回的现金净额'),
        # n_recp_disp_sobu	float	Y	处置子公司及其他营业单位收到的现金净额
        MetricsMeta('n_recp_disp_sobu', Crawl(
            'cashflow', 'n_recp_disp_sobu'), display='处置子公司及其他营业单位收到的现金净额'),
        # stot_inflows_inv_act	float	Y	投资活动现金流入小计
        MetricsMeta('stot_inflows_inv_act', Crawl(
            'cashflow', 'stot_inflows_inv_act'), display='投资活动现金流入小计'),
        # c_pay_acq_const_fiolta	float	Y	购建固定资产、无形资产和其他长期资产支付的现金
        MetricsMeta('c_pay_acq_const_fiolta',
                    Crawl('cashflow', 'c_pay_acq_const_fiolta'),
                    display='购建固定资产、无形资产和其他长期资产支付的现金'),
        # c_paid_invest	float	Y	投资支付的现金
        MetricsMeta('c_paid_invest', Crawl(
            'cashflow', 'c_paid_invest'), display='投资支付的现金'),
        # n_disp_subs_oth_biz	float	Y	取得子公司及其他营业单位支付的现金净额
        MetricsMeta('n_disp_subs_oth_biz', Crawl(
            'cashflow', 'n_disp_subs_oth_biz'), display='取得子公司及其他营业单位支付的现金净额'),
        # oth_pay_ral_inv_act	float	Y	支付其他与投资活动有关的现金
        MetricsMeta('oth_pay_ral_inv_act', Crawl(
            'cashflow', 'oth_pay_ral_inv_act'), display='支付其他与投资活动有关的现金'),
        # n_incr_pledge_loan	float	Y	质押贷款净增加额
        MetricsMeta('n_incr_pledge_loan', Crawl(
            'cashflow', 'n_incr_pledge_loan'), display='质押贷款净增加额'),
        # stot_out_inv_act	float	Y	投资活动现金流出小计
        MetricsMeta('stot_out_inv_act', Crawl(
            'cashflow', 'stot_out_inv_act'), display='投资活动现金流出小计'),
        # n_cashflow_inv_act	float	Y	投资活动产生的现金流量净额
        MetricsMeta('n_cashflow_inv_act', Crawl(
            'cashflow', 'n_cashflow_inv_act'), display='投资活动产生的现金流量净额'),
        # c_recp_borrow	float	Y	取得借款收到的现金
        MetricsMeta('c_recp_borrow', Crawl(
            'cashflow', 'c_recp_borrow'), display='取得借款收到的现金'),
        # proc_issue_bonds	float	Y	发行债券收到的现金
        MetricsMeta('proc_issue_bonds', Crawl(
            'cashflow', 'proc_issue_bonds'), display='发行债券收到的现金'),
        # oth_cash_recp_ral_fnc_act	float	Y	收到其他与筹资活动有关的现金
        MetricsMeta('oth_cash_recp_ral_fnc_act',
                    Crawl('cashflow', 'oth_cash_recp_ral_fnc_act'),
                    display='收到其他与筹资活动有关的现金'),
        # stot_cash_in_fnc_act	float	Y	筹资活动现金流入小计
        MetricsMeta('stot_cash_in_fnc_act', Crawl(
            'cashflow', 'stot_cash_in_fnc_act'), display='筹资活动现金流入小计'),
        # free_cashflow	float	Y	企业自由现金流量
        MetricsMeta('free_cashflow', Crawl(
            'cashflow', 'free_cashflow'), display='企业自由现金流量'),
        # c_prepay_amt_borr	float	Y	偿还债务支付的现金
        MetricsMeta('c_prepay_amt_borr', Crawl(
            'cashflow', 'c_prepay_amt_borr'), display='偿还债务支付的现金'),
        # c_pay_dist_dpcp_int_exp	float	Y	分配股利、利润或偿付利息支付的现金
        MetricsMeta('c_pay_dist_dpcp_int_exp',
                    Crawl('cashflow', 'c_pay_dist_dpcp_int_exp'),
                    display='分配股利、利润或偿付利息支付的现金'),
        # incl_dvd_profit_paid_sc_ms	float	Y	其中:子公司支付给少数股东的股利、利润
        MetricsMeta('incl_dvd_profit_paid_sc_ms',
                    Crawl('cashflow', 'incl_dvd_profit_paid_sc_ms'),
                    display='子公司支付给少数股东的股利、利润'),
        # oth_cashpay_ral_fnc_act	float	Y	支付其他与筹资活动有关的现金
        MetricsMeta('oth_cashpay_ral_fnc_act',
                    Crawl('cashflow', 'oth_cashpay_ral_fnc_act'),
                    display='支付其他与筹资活动有关的现金'),
        # stot_cashout_fnc_act	float	Y	筹资活动现金流出小计
        MetricsMeta('stot_cashout_fnc_act', Crawl(
            'cashflow', 'stot_cashout_fnc_act'), display='筹资活动现金流出小计'),
        # n_cash_flows_fnc_act	float	Y	筹资活动产生的现金流量净额
        MetricsMeta('n_cash_flows_fnc_act', Crawl(
            'cashflow', 'n_cash_flows_fnc_act'), display='筹资活动产生的现金流量净额'),
        # eff_fx_flu_cash	float	Y	汇率变动对现金的影响
        MetricsMeta('eff_fx_flu_cash', Crawl(
            'cashflow', 'eff_fx_flu_cash'), display='汇率变动对现金的影响'),
        # n_incr_cash_cash_equ	float	Y	现金及现金等价物净增加额
        MetricsMeta('n_incr_cash_cash_equ', Crawl(
            'cashflow', 'n_incr_cash_cash_equ'), display='现金及现金等价物净增加额'),
        # c_cash_equ_beg_period	float	Y	期初现金及现金等价物余额
        MetricsMeta('c_cash_equ_beg_period', Crawl(
            'cashflow', 'c_cash_equ_beg_period'), display='期初现金及现金等价物余额'),
        # c_cash_equ_end_period	float	Y	期末现金及现金等价物余额
        MetricsMeta('c_cash_equ_end_period', Crawl(
            'cashflow', 'c_cash_equ_end_period'), display='期末现金及现金等价物余额'),
        # c_recp_cap_contrib	float	Y	吸收投资收到的现金
        MetricsMeta('c_recp_cap_contrib', Crawl(
            'cashflow', 'c_recp_cap_contrib'), display='吸收投资收到的现金'),
        # incl_cash_rec_saims	float	Y	其中:子公司吸收少数股东投资收到的现金
        MetricsMeta('incl_cash_rec_saims', Crawl(
            'cashflow', 'incl_cash_rec_saims'), display='子公司吸收少数股东投资收到的现金'),
        # uncon_invest_loss	float	Y	未确认投资损失
        MetricsMeta('uncon_invest_loss', Crawl(
            'cashflow', 'uncon_invest_loss'), display='未确认投资损失'),
        # prov_depr_assets	float	Y	加:资产减值准备
        MetricsMeta('prov_depr_assets', Crawl(
            'cashflow', 'prov_depr_assets'), display='资产减值准备'),
        # depr_fa_coga_dpba	float	Y	固定资产折旧、油气资产折耗、生产性生物资产折旧
        MetricsMeta('depr_fa_coga_dpba', Crawl(
            'cashflow', 'depr_fa_coga_dpba'), display='固定资产折旧、油气资产折耗、生产性生物资产折旧'),
        # amort_intang_assets	float	Y	无形资产摊销
        MetricsMeta('amort_intang_assets', Crawl(
            'cashflow', 'amort_intang_assets'), display='无形资产摊销'),
        # lt_amort_deferred_exp	float	Y	长期待摊费用摊销
        MetricsMeta('lt_amort_deferred_exp', Crawl(
            'cashflow', 'lt_amort_deferred_exp'), display='长期待摊费用摊销'),
        # decr_deferred_exp	float	Y	待摊费用减少
        MetricsMeta('decr_deferred_exp', Crawl(
            'cashflow', 'decr_deferred_exp'), display='待摊费用减少'),
        # incr_acc_exp	float	Y	预提费用增加
        MetricsMeta('incr_acc_exp', Crawl(
            'cashflow', 'incr_acc_exp'), display='预提费用增加'),
        # loss_disp_fiolta	float	Y	处置固定、无形资产和其他长期资产的损失
        MetricsMeta('loss_disp_fiolta', Crawl(
            'cashflow', 'loss_disp_fiolta'), display='处置固定、无形资产和其他长期资产的损失'),
        # loss_scr_fa	float	Y	固定资产报废损失
        MetricsMeta('loss_scr_fa', Crawl(
            'cashflow', 'loss_scr_fa'), display='固定资产报废损失'),
        # loss_fv_chg	float	Y	公允价值变动损失
        MetricsMeta('loss_fv_chg', Crawl(
            'cashflow', 'loss_fv_chg'), display='公允价值变动损失'),
        # invest_loss	float	Y	投资损失
        MetricsMeta('invest_loss', Crawl(
            'cashflow', 'invest_loss'), display='投资损失'),
        # decr_def_inc_tax_assets	float	Y	递延所得税资产减少
        MetricsMeta('decr_def_inc_tax_assets',
                    Crawl('cashflow', 'decr_def_inc_tax_assets'),
                    display='递延所得税资产减少'),
        # incr_def_inc_tax_liab	float	Y	递延所得税负债增加
        MetricsMeta('incr_def_inc_tax_liab', Crawl(
            'cashflow', 'incr_def_inc_tax_liab'), display='递延所得税负债增加'),
        # decr_inventories	float	Y	存货的减少
        MetricsMeta('decr_inventories', Crawl(
            'cashflow', 'decr_inventories'), display='存货的减少'),
        # decr_oper_payable	float	Y	经营性应收项目的减少
        MetricsMeta('decr_oper_payable', Crawl(
            'cashflow', 'decr_oper_payable'), display='经营性应收项目的减少'),
        # incr_oper_payable	float	Y	经营性应付项目的增加
        MetricsMeta('incr_oper_payable', Crawl(
            'cashflow', 'incr_oper_payable'), display='经营性应付项目的增加'),
        # others	float	Y	其他
        MetricsMeta('others', Crawl('cashflow', 'others'), display='其他'),
        # im_net_cashflow_oper_act	float	Y	经营活动产生的现金流量净额(间接法)
        MetricsMeta('im_net_cashflow_oper_act',
                    Crawl('cashflow', 'im_net_cashflow_oper_act'),
                    display='经营活动产生的现金流量净额(间接法)'),
        # conv_debt_into_cap	float	Y	债务转为资本
        MetricsMeta('conv_debt_into_cap', Crawl(
            'cashflow', 'conv_debt_into_cap'), display='债务转为资本'),
        # conv_copbonds_due_within_1y	float	Y	一年内到期的可转换公司债券
        MetricsMeta('conv_copbonds_due_within_1y',
                    Crawl('cashflow', 'conv_copbonds_due_within_1y'),
                    display='一年内到期的可转换公司债券'),
        # fa_fnc_leases	float	Y	融资租入固定资产
        MetricsMeta('fa_fnc_leases', Crawl(
            'cashflow', 'fa_fnc_leases'), display='融资租入固定资产'),
        # end_bal_cash	float	Y	现金的期末余额
        MetricsMeta('end_bal_cash', Crawl(
            'cashflow', 'end_bal_cash'), display='现金的期末余额'),
        # beg_bal_cash	float	Y	减:现金的期初余额
        MetricsMeta('beg_bal_cash', Crawl(
            'cashflow', 'beg_bal_cash'), display='现金的期初余额'),
        # end_bal_cash_equ	float	Y	加:现金等价物的期末余额
        MetricsMeta('end_bal_cash_equ', Crawl(
            'cashflow', 'end_bal_cash_equ'), display='现金等价物的期末余额'),
        # beg_bal_cash_equ	float	Y	减:现金等价物的期初余额
        MetricsMeta('beg_bal_cash_equ', Crawl(
            'cashflow', 'beg_bal_cash_equ'), display='现金等价物的期初余额'),
        # im_n_incr_cash_equ	float	Y	现金及现金等价物净增加额(间接法)
        MetricsMeta('im_n_incr_cash_equ', Crawl(
            'cashflow', 'im_n_incr_cash_equ'), display='现金及现金等价物净增加额(间接法)')
    ]
    return metas
