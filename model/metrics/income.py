from model.stock import MetricsMeta
from model.expr.crawl import Crawl


def metrics():
    metas = [
        # total_revenue	float	Y	营业总收入
        MetricsMeta("total_revenue", Crawl("total_revenue")),
        # revenue	float	Y	营业收入
        MetricsMeta("revenue", Crawl("revenue")),
        # int_income	float	Y	利息收入
        MetricsMeta("int_income", Crawl("int_income")),
        # prem_earned	float	Y	已赚保费
        MetricsMeta("prem_earned", Crawl("prem_earned")),
        # comm_income	float	Y	手续费及佣金收入
        MetricsMeta("comm_income", Crawl("comm_income")),
        # n_commis_income	float	Y	手续费及佣金净收入
        MetricsMeta("n_commis_income", Crawl("n_commis_income")),
        # n_oth_income	float	Y	其他经营净收益
        MetricsMeta("n_oth_income", Crawl("n_oth_income")),
        # n_oth_b_income	float	Y	加:其他业务净收益
        MetricsMeta("n_oth_b_income", Crawl("n_oth_b_income")),
        # prem_income	float	Y	保险业务收入
        MetricsMeta("prem_income", Crawl("prem_income")),
        # out_prem	float	Y	减:分出保费
        MetricsMeta("out_prem", Crawl("out_prem")),
        # une_prem_reser	float	Y	提取未到期责任准备金
        MetricsMeta("une_prem_reser", Crawl("une_prem_reser")),
        # reins_income	float	Y	其中:分保费收入
        MetricsMeta("reins_income", Crawl("reins_income")),
        # n_sec_tb_income	float	Y	代理买卖证券业务净收入
        MetricsMeta("n_sec_tb_income", Crawl("n_sec_tb_income")),
        # n_sec_uw_income	float	Y	证券承销业务净收入
        MetricsMeta("n_sec_uw_income", Crawl("n_sec_uw_income")),
        # n_asset_mg_income	float	Y	受托客户资产管理业务净收入
        MetricsMeta("n_asset_mg_income", Crawl("n_asset_mg_income")),
        # oth_b_income	float	Y	其他业务收入
        MetricsMeta("oth_b_income", Crawl("oth_b_income")),
        # fv_value_chg_gain	float	Y	加:公允价值变动净收益
        MetricsMeta("fv_value_chg_gain", Crawl("fv_value_chg_gain")),
        # fv_value_chg_gain	float	Y	加:投资净收益
        MetricsMeta("fv_value_chg_gain", Crawl("fv_value_chg_gain")),
        # ass_invest_income	float	Y	其中:对联营企业和合营企业的投资收益
        MetricsMeta("ass_invest_income", Crawl("ass_invest_income")),
        # forex_gain	float	Y	加:汇兑净收益
        MetricsMeta("forex_gain", Crawl("forex_gain")),
        # total_cogs	float	Y	营业总成本
        MetricsMeta("total_cogs", Crawl("total_cogs")),
        # oper_cost	float	Y	减:营业成本
        MetricsMeta("oper_cost", Crawl("oper_cost")),
        # int_exp	float	Y	减:利息支出
        MetricsMeta("int_exp", Crawl("int_exp")),
        # comm_exp	float	Y	减:手续费及佣金支出
        MetricsMeta("comm_exp", Crawl("comm_exp")),
        # biz_tax_surchg	float	Y	减:营业税金及附加
        MetricsMeta("biz_tax_surchg", Crawl("biz_tax_surchg")),
        # sell_exp	float	Y	减:销售费用
        MetricsMeta("sell_exp", Crawl("sell_exp")),
        # admin_exp	float	Y	减:管理费用
        MetricsMeta("revadmin_expenue", Crawl("admin_exp")),
        # fin_exp	float	Y	减:财务费用
        MetricsMeta("fin_exp", Crawl("fin_exp")),
        # assets_impair_loss	float	Y	减:资产减值损失
        MetricsMeta("reveassets_impair_lossnue",
                      Crawl("assets_impair_loss")),
        # prem_refund	float	Y	退保金
        MetricsMeta("prem_refund", Crawl("prem_refund")),
        # compens_payout	float	Y	赔付总支出
        MetricsMeta("compens_payout", Crawl("compens_payout")),
        # reser_insur_liab	float	Y	提取保险责任准备金
        MetricsMeta("reser_insur_liab", Crawl("reser_insur_liab")),
        # div_payt	float	Y	保户红利支出
        MetricsMeta("div_payt", Crawl("div_payt")),
        # reins_exp	float	Y	分保费用
        MetricsMeta("reins_exp", Crawl("reins_exp")),
        # oper_exp	float	Y	营业支出
        MetricsMeta("oper_exp", Crawl("oper_exp")),
        # compens_payout_refu	float	Y	减:摊回赔付支出
        MetricsMeta("compens_payout_refu", Crawl("compens_payout_refu")),
        # insur_reser_refu	float	Y	减:摊回保险责任准备金
        MetricsMeta("insur_reser_refu", Crawl("insur_reser_refu")),
        # reins_cost_refund	float	Y	减:摊回分保费用
        MetricsMeta("reins_cost_refund", Crawl("reins_cost_refund")),
        # other_bus_cost	float	Y	其他业务成本
        MetricsMeta("other_bus_cost", Crawl("other_bus_cost")),
        # operate_profit	float	Y	营业利润
        MetricsMeta("operate_profit", Crawl("operate_profit")),
        # non_oper_income	float	Y	加:营业外收入
        MetricsMeta("non_oper_income", Crawl("non_oper_income")),
        # non_oper_exp	float	Y	减:营业外支出
        MetricsMeta("non_oper_exp", Crawl("non_oper_exp")),
        # nca_disploss	float	Y	其中:减:非流动资产处置净损失
        MetricsMeta("nca_disploss", Crawl("nca_disploss")),
        # total_profit	float	Y	利润总额
        MetricsMeta("total_profit", Crawl("total_profit")),
        # income_tax	float	Y	所得税费用
        MetricsMeta("income_tax", Crawl("income_tax")),
        # n_income	float	Y	净利润(含少数股东损益)
        MetricsMeta("n_income", Crawl("n_income")),
        # n_income_attr_p	float	Y	净利润(不含少数股东损益)
        MetricsMeta("n_income_attr_p", Crawl("n_income_attr_p")),
        # minority_gain	float	Y	少数股东损益
        MetricsMeta("minority_gain", Crawl("minority_gain")),
        # oth_compr_income	float	Y	其他综合收益
        MetricsMeta("oth_compr_income", Crawl("oth_compr_income")),
        # t_compr_income	float	Y	综合收益总额
        MetricsMeta("t_compr_income", Crawl("t_compr_income")),
        # compr_inc_attr_p	float	Y	归属于母公司(或股东)的综合收益总额
        MetricsMeta("compr_inc_attr_p", Crawl("compr_inc_attr_p")),
        # compr_inc_attr_m_s	float	Y	归属于少数股东的综合收益总额
        MetricsMeta("compr_inc_attr_m_s", Crawl("compr_inc_attr_m_s")),
        # ebit	float	Y	息税前利润
        MetricsMeta("ebit", Crawl("ebit")),
        # ebitda	float	Y	息税折旧摊销前利润
        MetricsMeta("ebitda", Crawl("ebitda")),
        # insurance_exp	float	Y	保险业务支出
        MetricsMeta("insurance_exp", Crawl("insurance_exp")),
        # undist_profit	float	Y	年初未分配利润
        MetricsMeta("undist_profit", Crawl("undist_profit")),
        # distable_profit	float	Y	可分配利润
        MetricsMeta("distable_profit", Crawl("distable_profit"))
    ]
    return metas
