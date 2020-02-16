from stockpy.metrics.base import MetricsMeta
from stockpy.expr import Crawl


def metrics():
    metas = [
        # total_revenue	float	Y	营业总收入
        MetricsMeta('total_revenue', Crawl(
            'income', 'total_revenue'), display='营业总收入'),
        # revenue	float	Y	营业收入
        MetricsMeta('revenue', Crawl('income', 'revenue'), display='营业收入'),
        # int_income	float	Y	利息收入
        MetricsMeta('int_income', Crawl(
            'income', 'int_income'), display='利息收入'),
        # prem_earned	float	Y	已赚保费
        MetricsMeta('prem_earned', Crawl(
            'income', 'prem_earned'), display='已赚保费'),
        # comm_income	float	Y	手续费及佣金收入
        MetricsMeta('comm_income', Crawl(
            'income', 'comm_income'), display='手续费及佣金收入'),
        # n_commis_income	float	Y	手续费及佣金净收入
        MetricsMeta('n_commis_income', Crawl(
            'income', 'n_commis_income'), display='手续费及佣金净收入'),
        # n_oth_income	float	Y	其他经营净收益
        MetricsMeta('n_oth_income', Crawl(
            'income', 'n_oth_income'), display='其他经营净收益'),
        # n_oth_b_income	float	Y	加:其他业务净收益
        MetricsMeta('n_oth_b_income', Crawl(
            'income', 'n_oth_b_income'), display='其他业务净收益'),
        # prem_income	float	Y	保险业务收入
        MetricsMeta('prem_income', Crawl(
            'income', 'prem_income'), display='保险业务收入'),
        # out_prem	float	Y	减:分出保费
        MetricsMeta('out_prem', Crawl('income', 'out_prem'), display='分出保费'),
        # une_prem_reser	float	Y	提取未到期责任准备金
        MetricsMeta('une_prem_reser', Crawl(
            'income', 'une_prem_reser'), display='提取未到期责任准备金'),
        # reins_income	float	Y	其中:分保费收入
        MetricsMeta('reins_income', Crawl(
            'income', 'reins_income'), display='分保费收入'),
        # n_sec_tb_income	float	Y	代理买卖证券业务净收入
        MetricsMeta('n_sec_tb_income', Crawl(
            'income', 'n_sec_tb_income'), display='代理买卖证券业务净收入'),
        # n_sec_uw_income	float	Y	证券承销业务净收入
        MetricsMeta('n_sec_uw_income', Crawl(
            'income', 'n_sec_uw_income'), display='证券承销业务净收入'),
        # n_asset_mg_income	float	Y	受托客户资产管理业务净收入
        MetricsMeta('n_asset_mg_income', Crawl(
            'income', 'n_asset_mg_income'), display='受托客户资产管理业务净收入'),
        # oth_b_income	float	Y	其他业务收入
        MetricsMeta('oth_b_income', Crawl(
            'income', 'oth_b_income'), display='其他业务收入'),
        # fv_value_chg_gain	float	Y	加:公允价值变动净收益
        MetricsMeta('fv_value_chg_gain', Crawl(
            'income', 'fv_value_chg_gain'), display='公允价值变动净收益'),
        # fv_value_chg_gain	float	Y	加:投资净收益
        MetricsMeta('fv_value_chg_gain', Crawl(
            'income', 'fv_value_chg_gain'), display='投资净收益'),
        # ass_invest_income	float	Y	其中:对联营企业和合营企业的投资收益
        MetricsMeta('ass_invest_income', Crawl(
            'income', 'ass_invest_income'), display='对联营企业和合营企业的投资收益'),
        # forex_gain	float	Y	加:汇兑净收益
        MetricsMeta('forex_gain', Crawl(
            'income', 'forex_gain'), display='汇兑净收益'),
        # total_cogs	float	Y	营业总成本
        MetricsMeta('total_cogs', Crawl(
            'income', 'total_cogs'), display='营业总成本'),
        # oper_cost	float	Y	减:营业成本
        MetricsMeta('oper_cost', Crawl('income', 'oper_cost'), display='营业成本'),
        # int_exp	float	Y	减:利息支出
        MetricsMeta('int_exp', Crawl('income', 'int_exp'), display='利息支出'),
        # comm_exp	float	Y	减:手续费及佣金支出
        MetricsMeta('comm_exp', Crawl(
            'income', 'comm_exp'), display='手续费及佣金支出'),
        # biz_tax_surchg	float	Y	减:营业税金及附加
        MetricsMeta('biz_tax_surchg', Crawl(
            'income', 'biz_tax_surchg'), display='营业税金及附加'),
        # sell_exp	float	Y	减:销售费用
        MetricsMeta('sell_exp', Crawl('income', 'sell_exp'), display='销售费用'),
        # admin_exp	float	Y	减:管理费用
        MetricsMeta('admin_exp', Crawl('income', 'admin_exp'), display='管理费用'),
        # fin_exp	float	Y	减:财务费用
        MetricsMeta('fin_exp', Crawl('income', 'fin_exp'), display='财务费用'),
        # assets_impair_loss	float	Y	减:资产减值损失
        MetricsMeta('assets_impair_lossnue',
                    Crawl('income', 'assets_impair_loss'), display='资产减值损失'),
        # prem_refund	float	Y	退保金
        MetricsMeta('prem_refund', Crawl(
            'income', 'prem_refund'), display='退保金'),
        # compens_payout	float	Y	赔付总支出
        MetricsMeta('compens_payout', Crawl(
            'income', 'compens_payout'), display='赔付总支出'),
        # reser_insur_liab	float	Y	提取保险责任准备金
        MetricsMeta('reser_insur_liab', Crawl(
            'income', 'reser_insur_liab'), display='提取保险责任准备金'),
        # div_payt	float	Y	保户红利支出
        MetricsMeta('div_payt', Crawl('income', 'div_payt'), display='保户红利支出'),
        # reins_exp	float	Y	分保费用
        MetricsMeta('reins_exp', Crawl('income', 'reins_exp'), display='分保费用'),
        # oper_exp	float	Y	营业支出
        MetricsMeta('oper_exp', Crawl('income', 'oper_exp'), display='营业支出'),
        # compens_payout_refu	float	Y	减:摊回赔付支出
        MetricsMeta('compens_payout_refu', Crawl(
            'income', 'compens_payout_refu'), display='摊回赔付支出'),
        # insur_reser_refu	float	Y	减:摊回保险责任准备金
        MetricsMeta('insur_reser_refu', Crawl(
            'income', 'insur_reser_refu'), display='摊回保险责任准备金'),
        # reins_cost_refund	float	Y	减:摊回分保费用
        MetricsMeta('reins_cost_refund', Crawl(
            'income', 'reins_cost_refund'), display='摊回分保费用'),
        # other_bus_cost	float	Y	其他业务成本
        MetricsMeta('other_bus_cost', Crawl(
            'income', 'other_bus_cost'), display='其他业务成本'),
        # operate_profit	float	Y	营业利润
        MetricsMeta('operate_profit', Crawl(
            'income', 'operate_profit'), display='营业利润'),
        # non_oper_income	float	Y	加:营业外收入
        MetricsMeta('non_oper_income', Crawl(
            'income', 'non_oper_income'), display='营业外收入'),
        # non_oper_exp	float	Y	减:营业外支出
        MetricsMeta('non_oper_exp', Crawl(
            'income', 'non_oper_exp'), display='营业外支出'),
        # nca_disploss	float	Y	其中:减:非流动资产处置净损失
        MetricsMeta('nca_disploss', Crawl(
            'income', 'nca_disploss'), display='非流动资产处置净损失'),
        # total_profit	float	Y	利润总额
        MetricsMeta('total_profit', Crawl(
            'income', 'total_profit'), display='利润总额'),
        # income_tax	float	Y	所得税费用
        MetricsMeta('income_tax', Crawl(
            'income', 'income_tax'), display='所得税费用'),
        # n_income	float	Y	净利润(含少数股东损益)
        MetricsMeta('n_income', Crawl('income', 'n_income'),
                    display='净利润'),
        # n_income_attr_p	float	Y	净利润(不含少数股东损益)
        MetricsMeta('n_income_attr_p', Crawl(
            'income', 'n_income_attr_p'), display='净利润'),
        # minority_gain	float	Y	少数股东损益
        MetricsMeta('minority_gain', Crawl(
            'income', 'minority_gain'), display='少数股东损益'),
        # oth_compr_income	float	Y	其他综合收益
        MetricsMeta('oth_compr_income', Crawl(
            'income', 'oth_compr_income'), display='其他综合收益'),
        # t_compr_income	float	Y	综合收益总额
        MetricsMeta('t_compr_income', Crawl(
            'income', 't_compr_income'), display='综合收益总额'),
        # compr_inc_attr_p	float	Y	归属于母公司(或股东)的综合收益总额
        MetricsMeta('compr_inc_attr_p', Crawl(
            'income', 'compr_inc_attr_p'), display='归属于母公司(或股东)的综合收益总额'),
        # compr_inc_attr_m_s	float	Y	归属于少数股东的综合收益总额
        MetricsMeta('compr_inc_attr_m_s', Crawl(
            'income', 'compr_inc_attr_m_s'), display='归属于少数股东的综合收益总额'),
        # ebit	float	Y	息税前利润
        MetricsMeta('ebit', Crawl('income', 'ebit'), display='息税前利润'),
        # ebitda	float	Y	息税折旧摊销前利润
        MetricsMeta('ebitda', Crawl('income', 'ebitda'), display='息税折旧摊销前利润'),
        # insurance_exp	float	Y	保险业务支出
        MetricsMeta('insurance_exp', Crawl(
            'income', 'insurance_exp'), display='保险业务支出'),
        # undist_profit	float	Y	年初未分配利润
        MetricsMeta('undist_profit', Crawl(
            'income', 'undist_profit'), display='年初未分配利润'),
        # distable_profit	float	Y	可分配利润
        MetricsMeta('distable_profit', Crawl(
            'income', 'distable_profit'), display='可分配利润')
    ]
    return metas
