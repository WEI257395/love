# -*- coding: utf-8 -*-
import requests
import json
import random
from datetime import datetime, date
from zhdate import ZhDate

# --- 1. 配置区 ---
# 请在这里修改你的个人信息

# 企业微信机器人的Webhook地址
WEBHOOK_URL = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=f6a4a592-512e-4f9d-9944-70ced7e6dfd8"

# 和风天气的API Key
QWEATHER_KEY = "c9a29f7b879547269b3742d7edd7a660"

# 城市代码 (沈北新区)
LOCATION_ID = "101070113"

# 恋爱开始日期 (格式: YYYY-MM-DD)
LOVE_START_DATE = "2020-07-05"

# 女朋友的生日 (农历三月二十九)
GIRLFRIEND_BIRTHDAY = (3, 29)  # 农历三月二十九

# 你们的恋爱纪念日 (月, 日)
ANNIVERSARY_DAY = (7, 5)

# 小情话列表 (可以自己增加更多)
# 小情话列表 (可以自己增加更多)
LOVE_PHRASES = [
    "我想和你一起，看遍世间所有风景。",
    "遇见你，是我生命中最美的意外。",
    "我的世界因为你而变得明亮。",
    "与你共度的时光，是我最珍贵的回忆。",
    "每天醒来看到你，就是我最大的幸福。",
    "你的微笑，是我一天好心情的开始。",
    "无论未来怎样，我都会一直陪在你身边。",
    "你是我心中最亮的星，照亮我前行的路。",
    "和你在一起的每一天，都是情人节。",
    "你的存在，让我的世界变得完整。",
    "我想把所有的温柔都给你，因为只有你值得。",
    "你是我生命中最美好的奇迹。",
    "和你在一起，连空气都是甜的。",
    "你是我心中永远的小公主。",
    "我想和你一起慢慢变老，看遍人间烟火。",
    "你的每一个笑容，都是我收藏的珍宝。",
    "在我心中，你永远是最特别的那一个。",
    "和你在一起的时光，是我最珍贵的财富。",
    "你是我心中永远的阳光，温暖我的心房。",
    "我想和你一起，走过每一个春夏秋冬。",
    "你的温柔，是我最想守护的美好。",
    "和你在一起，每一天都是新的开始。",
    "你是我心中最完美的女孩。",
    "我想把全世界都给你，只要你开心。",
    "你的存在，让我的生活变得有意义。",
    "和你在一起，连平凡的日子都变得特别。",
    "你是我心中永远的小可爱。",
    "我想和你一起，创造属于我们的回忆。",
    "你的每一个眼神，都让我心动不已。",
    "和你在一起，是我最大的幸运。",
    # 新增的50条情话
    "你是我心跳的理由，呼吸的意义。",
    "爱上你，是我做过最正确的决定。",
    "你的名字，是我写过最短的情诗。",
    "我想住进你的心里，没有房租的那种。",
    "你一笑，我的世界就开满了花。",
    "有你在身边，风都是温柔的。",
    "你是我漫长人生中，最想拥抱的温暖。",
    "我愿意用一生来读懂你这本书。",
    "你的手是我最想牵的永远。",
    "你是我失眠时，最想见的那个人。",
    "遇见你之后，其他人都是将就。",
    "你是我藏在云层里的月亮，也是我穷其一生想要寻找的宝藏。",
    "我想和你分享所有的日出日落。",
    "你的声音，是我最爱的旋律。",
    "你是我平淡生活里最绚烂的烟火。",
    "我想变成风，轻轻拂过你的脸庞。",
    "有你的地方，就是我的家。",
    "你是我所有温柔的来源和归属。",
    "我喜欢你，像风走了八千里，不问归期。",
    "你是我青春里最热烈的篇章。",
    "我想和你一起吃很多很多顿饭。",
    "你的眼睛里有星辰大海，让我沉醉不已。",
    "你是我永不厌倦的欢喜。",
    "我想把整个夏天的阳光都送给你。",
    "有你在，每一天都值得期待。",
    "你是我最想留住的幸运。",
    "我想和你一起虚度时光，比如低头看鱼。",
    "你的存在，就是我热爱生活的原因。",
    "你是我梦中的常客，心中的挚爱。",
    "我想和你一起，从青丝到白发。",
    "你是我所有的不理智和毫不犹豫。",
    "有你的未来，我才充满期待。",
    "你是我最甜蜜的负担。",
    "我想把你宠成世界上最幸福的人。",
    "你的笑容，治愈我所有的不快乐。",
    "你是我人生中最美的风景线。",
    "我想和你一起数星星，直到天明。",
    "你是我拒绝所有人的唯一理由。",
    "有你在，冬天也变得温暖。",
    "你是我最想守护的美好梦想。",
    "我想和你一起，尝遍世间所有美食。",
    "你的温柔，是我戒不掉的瘾。",
    "你是我生命中最动人的旋律。",
    "我想把你写进我的未来计划里。",
    "有你的陪伴，我不再害怕孤独。",
    "你是我最珍贵的限量版。",
    "我想和你一起，把平凡的日子过成诗。",
    "你的出现，让我的世界有了色彩。",
    "你是我永不褪色的爱恋。",
    "我想和你一起，看遍世间繁华。"
]

# 温馨提示列表 (可以自己增加更多)
# 温馨提示列表 (可以自己增加更多)
WARM_TIPS = [
    "今天也要元气满满，记得按时吃饭喝水哦！",
    "工作再忙，也要注意休息，别太累了。",
    "天气变化快，注意增减衣物，别感冒啦。",
    "给你一个云抱抱，希望能带给你好心情！",
    "想你啦，期待下班见到你！",
    # 新增的50条温馨提示
    "记得给眼睛休息一下，看看远处的绿色植物吧～",
    "喝水时间到啦！保持水分对身体很重要哦！",
    "午休时间记得小憩一会儿，下午更有精神呢！",
    "出门前记得检查物品，别落下东西啦！",
    "今天也要记得微笑，好运总会眷顾爱笑的人！",
    "晚上早点休息，别熬夜玩手机啦！",
    "记得定期运动，保持身体健康最重要！",
    "心情不好的时候，记得我永远在这里陪你！",
    "吃饭要细嚼慢咽，对肠胃更好哦！",
    "今天也要对自己好一点，你值得被温柔对待！",
    "遇到困难别着急，慢慢来，总会解决的！",
    "站起来活动一下，放松肩颈吧！",
    "今天也要保持乐观，好事正在发生呢！",
    "记得多吃水果蔬菜，补充维生素哦！",
    "压力大的时候，深呼吸几次会好很多呢！",
    "今天也要给自己一点小奖励，你真的很棒！",
    "记得定期整理房间，整洁的环境会让心情更好！",
    "长时间用电脑，记得滴眼药水保护眼睛哦！",
    "今天也要记得感恩，珍惜身边的小确幸！",
    "遇到不开心的事，说出来会轻松很多！",
    "记得保持微笑，你的笑容真的很治愈！",
    "今天也要进步一点点，成为更好的自己！",
    "天气干燥，记得多涂护手霜保护双手！",
    "今天也要善待他人，传播正能量！",
    "晚上泡个热水脚，有助于睡眠哦！",
    "今天也要勇敢面对挑战，你可以的！",
    "记得给手机充电，保持联系畅通！",
    "保持好奇心，生活会有更多乐趣呢！",
    "今天也要学会放下，不要让烦恼过夜！",
    "记得定期体检，健康最重要！",
    "分享快乐，快乐就会变成双倍！",
    "今天也要保持善良，世界因你而美好！",
    "记得抬头看看天空，美丽的云彩在等你欣赏！",
    "保持学习的心态，每天都有新收获！",
    "今天也要珍惜当下，过好每一分钟！",
    "记得经常说谢谢，感恩让生活更美好！",
    "保持耐心，美好的事情值得等待！",
    "今天也要爱自己，你是独一无二的！",
    "记得保持希望，明天会更好！",
    "小小的进步也值得庆祝，你真棒！"
]

# 健康提醒列表
HEALTH_TIPS = [
    "保持心情愉快，笑容是最好的化妆品。",
    "注意用眼卫生，看屏幕久了要休息一下。",
    "保持室内空气流通，呼吸新鲜空气。",
    "记得按时吃饭，别让胃受委屈。",
    "多晒太阳，补充维生素D。",
    "保持规律的作息时间，身体会感谢你的。",
    "记得洗手，保持个人卫生。",
    "适当补充蛋白质，让身体更强壮。",
    "保持心情放松，压力大时要学会调节。",
    # 新增的50条健康温馨提示
    "每天散步30分钟，让身体活动起来吧！",
    "保持正确坐姿，保护脊椎健康很重要哦！",
    "记得定期开窗通风，让新鲜空气进来～",
    "睡前泡个热水脚，有助于提高睡眠质量！",
    "保持口腔卫生，早晚刷牙别忘了哦！",
    "适当做做伸展运动，缓解肌肉疲劳！",
    "记得定期修剪指甲，保持手部卫生！",
    "保持乐观心态，好事自然会发生！",
    "每天深呼吸几次，放松身心很有效！",
    "记得定期晒被子，阳光是最好的消毒剂！",
    "保持适当体重，健康美丽两不误！",
    "睡前少看手机，保护眼睛也助眠！",
    "记得多微笑，笑容能传染快乐哦！",
    "保持家居整洁，环境会影响心情呢！",
    "适当听听音乐，放松心情很有效！",
    "记得定期体检，早发现早预防！",
    "保持充足睡眠，美容养颜又健康！",
    "每天喝够8杯水，新陈代谢才会好！",
    "记得保护听力，不要长时间戴耳机！",
    "保持适度运动，生命在于运动呀！",
    "睡前喝杯温牛奶，有助于安神入睡！",
    "记得保护皮肤，做好保湿和防晒！",
    "保持良好姿势，避免颈椎问题！",
    "适当补充益生菌，肠道健康很重要！",
    "记得定期洗牙，口腔健康不能忽视！",
    "保持心情平静，遇事不要着急！",
    "每天吃几颗坚果，补充优质脂肪！",
    "记得保护膝盖，运动时要做好防护！",
    "保持适当社交，和朋友多联系哦！",
    "睡前做做瑜伽，放松身心助睡眠！",
    "记得多吃粗粮，促进肠道蠕动！",
    "保持室内湿度，避免空气太干燥！",
    "适当补充维生素，增强免疫力！",
    "记得保护腰部，搬重物要小心！",
    "保持良好卫生习惯，预防疾病传播！",
    "每天吃早餐，提供一天的能量！",
    "记得保护牙齿，少吃甜食和酸性食物！",
    "保持适度休息，劳逸结合最重要！",
    "适当补充钙质，强健骨骼和牙齿！",
    "记得保护眼睛，多吃胡萝卜和蓝莓！",
    "保持心情开朗，烦恼都会过去的！",
    "每天做些喜欢的事，让生活更有趣！",
    "记得保护耳朵，避免长时间噪音！",
    "保持适度紫外线，晒太阳要选时间！",
    "适当补充铁质，预防贫血哦！",
    "记得保护脚部，穿合适的鞋子！",
    "保持生活规律，生物钟很重要！",
    "每天给自己一个微笑，从心开始美好！"
]

# 锻炼提醒列表 (特别关注背部锻炼)
EXERCISE_TIPS = [
    "今天也要记得锻炼哦，特别是背部训练！",
    "背部肌肉很重要，记得做几组引体向上或划船动作！",
    "久坐后记得做几个背部拉伸，保护你的脊椎！",
    "背部训练不仅能塑形，还能改善体态，加油！",
    "记得做俯卧撑或平板支撑，锻炼核心和背部！",
    "背部肌肉强健，整个人都会更有气质！",
    "今天做几组背部训练吧，让身体更挺拔！",
    "记得做猫式伸展，放松背部肌肉！",
    "背部训练要坚持，每天进步一点点！",
    "做几个深蹲和硬拉，全身都会受益！",
    "背部训练不仅能塑形，还能预防腰背疼痛！",
    "记得做几组划船动作，让背部线条更美！",
    "背部肌肉是身体的支柱，要好好锻炼！",
    "今天做几组背部训练，让身体更健康！",
    "背部训练要坚持，效果会慢慢显现的！"
]

# 饮食提醒列表 (鼓励多吃饭)
DIET_TIPS = [
     "记得吃午餐，下午才有精神！",
    "多吃点好的，身体需要营养！",
    "不要为了身材而饿肚子，健康第一！",
    "记得吃晚餐，晚上也要有能量！",
    "多吃点有营养的，让身体更健康！",
    # 新增的50条饮食温馨提示
    "早餐要吃好，一天的精气神都靠它啦！",
    "吃饭要按时，胃也需要规律的作息呢！",
    "多吃蔬菜水果，补充维生素和纤维哦！",
    "记得细嚼慢咽，好好享受美食的滋味！",
    "少吃外卖，自己做饭更健康更卫生！",
    "多喝温水，促进新陈代谢对身体好！",
    "饮食要均衡，荤素搭配才营养全面！",
    "少吃辛辣刺激，保护肠胃很重要！",
    "记得补充蛋白质，鱼肉蛋奶都是好选择！",
    "不要暴饮暴食，七分饱最健康！",
    "多吃粗粮，有益肠道健康哦！",
    "少吃甜食，控糖对身体好处多！",
    "记得补钙，多喝牛奶多吃豆制品！",
    "吃饭时少看手机，专心享受美食吧！",
    "多喝汤水，滋润身体又养生！",
    "少吃油炸食品，清淡饮食更健康！",
    "记得多吃深海鱼，补充Omega-3！",
    "不要边吃饭边工作，好好休息一下！",
    "多吃色彩丰富的食物，营养更全面！",
    "记得少吃盐，控盐对血压好！",
    "多吃坚果，补充优质脂肪和微量元素！",
    "不要喝太多冷饮，保护脾胃很重要！",
    "记得吃早餐，开启元气满满的一天！",
    "多吃菌菇类，增强免疫力哦！",
    "少吃加工食品，新鲜食材最健康！",
    "记得多喝水，每天至少8杯水！",
    "多吃含铁食物，菠菜红枣都很棒！",
    "不要空腹喝咖啡，先吃点东西吧！",
    "记得少吃宵夜，让肠胃晚上休息！",
    "多吃当季食材，新鲜又营养！",
    "少吃腌制食品，新鲜才是最好的！",
    "记得补充维生素C，多吃橙子猕猴桃！",
    "吃饭要有规律，不要饥一顿饱一顿！",
    "多吃富含纤维的食物，帮助消化！",
    "少吃高热量零食，健康小零食更佳！",
    "记得喝酸奶，益生菌对肠道好！",
    "多吃豆制品，优质植物蛋白来源！",
    "不要挑食，各种营养都要补充！",
    "记得少喝含糖饮料，水是最佳选择！",
    "多吃含锌食物，贝壳类海鲜很不错！",
    "少吃肥肉，选择瘦肉更健康！",
    "记得多吃黑色食物，黑芝麻黑豆都很好！",
    "吃饭保持好心情，消化吸收会更好！",
    "多吃抗氧化食物，蓝莓绿茶都很棒！",
    "记得饮食多样化，不要总吃同样的东西！",
    "多吃温暖的食物，保护脾胃健康！"
]


# --- 代码区 (以下部分通常无需修改) ---

def get_weather():
    """获取天气信息，带重试机制"""
    url = f"https://devapi.qweather.com/v7/weather/3d?location={LOCATION_ID}&key={QWEATHER_KEY}"
    
    # 重试配置
    max_retries = 3
    timeout = 15  # 增加超时时间到15秒
    
    for attempt in range(max_retries):
        try:
            print(f"正在尝试获取天气信息... (第{attempt + 1}次尝试)")
            response = requests.get(url, timeout=timeout)
            response.raise_for_status()
            data = response.json()
            
            if data.get("code") == "200":
                daily_forecast = data['daily'][0]
                weather_info = {
                    'city': '沈北新区',
                    'date': daily_forecast['fxDate'],
                    'text_day': daily_forecast['textDay'],
                    'temp_max': daily_forecast['tempMax'],
                    'temp_min': daily_forecast['tempMin'],
                    'wind_dir': daily_forecast['windDirDay'],
                    'precip': daily_forecast.get('precip', '0'),
                }
                print(f"天气数据获取成功: {weather_info['text_day']} {weather_info['temp_min']}~{weather_info['temp_max']}°C")
                return weather_info
            else:
                print(f"天气API返回错误: {data.get('code', '未知错误')} - {data.get('code', '')}")
                if attempt < max_retries - 1:
                    print(f"等待2秒后重试...")
                    import time
                    time.sleep(2)
                    
        except requests.exceptions.Timeout as e:
            print(f"获取天气超时 (第{attempt + 1}次尝试): {e}")
            if attempt < max_retries - 1:
                print(f"等待3秒后重试...")
                import time
                time.sleep(3)
        except requests.exceptions.ConnectionError as e:
            print(f"网络连接错误 (第{attempt + 1}次尝试): {e}")
            if attempt < max_retries - 1:
                print(f"等待3秒后重试...")
                import time
                time.sleep(3)
        except requests.exceptions.RequestException as e:
            print(f"获取天气失败 (第{attempt + 1}次尝试): {e}")
            if attempt < max_retries - 1:
                print(f"等待2秒后重试...")
                import time
                time.sleep(2)
        except Exception as e:
            print(f"处理天气数据时出错 (第{attempt + 1}次尝试): {e}")
            if attempt < max_retries - 1:
                print(f"等待2秒后重试...")
                import time
                time.sleep(2)
    
    print("天气获取失败，已尝试所有重试次数")
    return None


def calculate_days():
    """计算恋爱天数和倒计时"""
    today = date.today()

    # 恋爱天数
    love_start = datetime.strptime(LOVE_START_DATE, "%Y-%m-%d").date()
    love_days = (today - love_start).days + 1

    # 农历生日倒计时
    try:
        # 获取今年的农历生日对应的公历日期
        birthday_this_year = ZhDate(today.year, GIRLFRIEND_BIRTHDAY[0], GIRLFRIEND_BIRTHDAY[1]).to_datetime().date()
        
        if birthday_this_year < today:
            # 如果今年生日已过，计算明年生日
            birthday_next_year = ZhDate(today.year + 1, GIRLFRIEND_BIRTHDAY[0], GIRLFRIEND_BIRTHDAY[1]).to_datetime().date()
            birthday_countdown = (birthday_next_year - today).days
        else:
            birthday_countdown = (birthday_this_year - today).days
    except:
        # 如果农历转换失败，使用公历作为备选
        birthday_this_year = date(today.year, GIRLFRIEND_BIRTHDAY[0], GIRLFRIEND_BIRTHDAY[1])
        if birthday_this_year < today:
            birthday_next_year = date(today.year + 1, GIRLFRIEND_BIRTHDAY[0], GIRLFRIEND_BIRTHDAY[1])
            birthday_countdown = (birthday_next_year - today).days
        else:
            birthday_countdown = (birthday_this_year - today).days

    # 纪念日倒计时
    anniversary_this_year = date(today.year, ANNIVERSARY_DAY[0], ANNIVERSARY_DAY[1])
    if anniversary_this_year < today:
        anniversary_next_year = date(today.year + 1, ANNIVERSARY_DAY[0], ANNIVERSARY_DAY[1])
        anniversary_countdown = (anniversary_next_year - today).days
    else:
        anniversary_countdown = (anniversary_this_year - today).days

    return {
        'love_days': love_days,
        'birthday_countdown': birthday_countdown,
        'anniversary_countdown': anniversary_countdown
    }


def get_health_reminder(weather_data):
    """根据天气和季节生成健康提醒"""
    today = date.today()
    month = today.month
    
    # 基础健康提醒
    health_tip = random.choice(HEALTH_TIPS)
    
    # 根据天气调整提醒
    if weather_data:
        temp_max = int(weather_data['temp_max'])
        temp_min = int(weather_data['temp_min'])
        weather_text = weather_data['text_day']
        
        # 温度相关提醒
        if temp_max > 30:
            health_tip = "天气炎热，记得多喝水，避免中暑哦！"
        elif temp_min < 0:
            health_tip = "天气寒冷，注意保暖，多穿衣服！"
        elif temp_max - temp_min > 10:
            health_tip = "早晚温差大，记得及时增减衣物！"
        
        # 天气类型相关提醒
        if '雨' in weather_text or '雪' in weather_text:
            health_tip = "今天有降水，出门记得带伞，注意安全！"
        elif '晴' in weather_text and temp_max > 25:
            health_tip = "阳光明媚，记得防晒，多补充水分！"
        elif '雾' in weather_text or '霾' in weather_text:
            health_tip = "空气质量不太好，减少户外活动，记得戴口罩！"
    
    # 根据季节调整提醒
    if month in [12, 1, 2]:  # 冬季
        if not weather_data or '雨' not in weather_data['text_day']:
            health_tip = "冬季干燥，记得多喝水，注意保湿！"
    elif month in [3, 4, 5]:  # 春季
        health_tip = "春暖花开，适合户外运动，但要注意花粉过敏！"
    elif month in [6, 7, 8]:  # 夏季
        health_tip = "夏季炎热，注意防暑降温，多吃清淡食物！"
    elif month in [9, 10, 11]:  # 秋季
        health_tip = "秋高气爽，适合运动，但要注意早晚温差！"
    
    return health_tip


def get_exercise_reminder():
    """获取锻炼提醒，特别关注背部锻炼"""
    return random.choice(EXERCISE_TIPS)


def get_diet_reminder():
    """获取饮食提醒，鼓励多吃饭"""
    return random.choice(DIET_TIPS)


def build_message():
    """构造最终要发送的消息"""
    days_data = calculate_days()
    weather_data = get_weather()

    today_str = date.today().strftime('%Y年%m月%d日')

    # 构造天气部分
    weather_str = "> **今日天气提醒** 🌤️\n"
    if weather_data:
        tip = "天气不错！"
        if int(weather_data['temp_max']) - int(weather_data['temp_min']) > 8:
            tip = "但早晚温差大，记得加件外套哦！"
        if float(weather_data['precip']) > 0:
            tip = "今天可能会下雨，出门记得带伞哦！"

        weather_str += f"> ● 城市：{weather_data['city']}\n" \
                       f"> ● 天气：{weather_data['text_day']}\n" \
                       f"> ● 温度：{weather_data['temp_min']} ~ {weather_data['temp_max']}°C\n" \
                       f"> ● 风向：{weather_data['wind_dir']}\n" \
                       f"> ● 温馨提示：{tip}"
    else:
        weather_str += "> 获取天气失败了，但我的爱不会断线！"

    # 构造纪念日部分
    anniversary_str = f"> **我们的纪念日** ❤️\n" \
                      f"> ● 距离宝宝的农历生日🎂还有 **{days_data['birthday_countdown']}** 天！\n" \
                      f"> ● 距离我们的恋爱纪念日还有 **{days_data['anniversary_countdown']}** 天！"

    # 随机选择情话和提示
    love_phrase = random.choice(LOVE_PHRASES)
    warm_tip = random.choice(WARM_TIPS)
    
    # 获取各种提醒
    health_tip = get_health_reminder(weather_data)
    exercise_tip = get_exercise_reminder()
    diet_tip = get_diet_reminder()

    # 拼接完整消息
    content = f"### 💕亲爱的宝宝，早上好！💕\n\n" \
              f"今天是 **{today_str}**，是我们相爱的第 **{days_data['love_days']}** 天！\n\n" \
              f"{weather_str}\n\n" \
              f"{anniversary_str}\n\n" \
              f"> **一句悄悄话** 💌\n" \
              f"> {love_phrase}\n\n" \
              f"> **今日份关心** ❤️\n" \
              f"> {warm_tip}\n\n" \
              f"> **健康小贴士** 🏥\n" \
              f"> {health_tip}\n\n" \
              f"> **锻炼提醒** 💪\n" \
              f"> {exercise_tip}\n\n" \
              f"> **饮食提醒** 🍎\n" \
              f"> {diet_tip}"

    message = {
        "msgtype": "markdown",
        "markdown": {
            "content": content
        }
    }
    return message


def send_message(message):
    """发送消息到企业微信机器人"""
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(WEBHOOK_URL, data=json.dumps(message), headers=headers, timeout=10)
        if response.json().get("errcode") == 0:
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - 消息发送成功！")
        else:
            print(f"消息发送失败：{response.text}")
    except requests.exceptions.RequestException as e:
        print(f"网络请求错误: {e}")


if __name__ == "__main__":
    final_message = build_message()
    send_message(final_message)