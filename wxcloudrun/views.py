from flask import render_template, request, jsonify
from run import app
from wxcloudrun.model import LogisticsInfo


@app.route('/')
def index():
    """
    :return: 返回index页面
    """
    return render_template('index.html')


@app.route('/api/query-logistics', methods=['POST'])
def query_logistics():
    """
    查询物流信息
    :return: 返回物流单号和快递公司名称
    """
    # 获取请求参数
    params = request.get_json()

    # 检查手机号参数
    if 'phone' not in params:
        return jsonify({"error": "缺少手机号"}), 400

    phone = params['phone']

    # 查询物流信息
    logistics = LogisticsInfo.query.filter_by(phone=phone).first()
    if logistics:
        return jsonify({
            "tracking_number": logistics.tracking_number,
            "courier_company": logistics.courier_company
        })
    else:
        return jsonify({"error": "未找到物流信息"}), 404
