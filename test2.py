import tensorflow as tf

def x2_plus_b(x, b):
    # 関数の第一引数 x を出力する _x という名前の定数型のopを定義
    _x = tf.constant(x)
    # 関数の第二引数 b を出力する _b という名前の定数型のopを定義
    _b = tf.constant(b)
    # resultに_xの2乗を代入
    result = tf.square(_x)
    # resultに_bを加算
    result = tf.add(result, _b)
    # resultを返す
    return result

def monitor_calculation(x, b):
    title = "b = {0}".format(b)
    c = x2_plus_b(float(x), float(b))
    s = tf.scalar_summary(title, c)
    m = tf.merge_summary([s])  # if you are using some summaries, merge them
    return m

with tf.Session() as sess:
    writer = tf.train.SummaryWriter("log", graph=sess.graph)
    xaxis = range(-10, 12)

    for b in range(3):
        for x in xaxis:
            summary_str = sess.run(monitor_calculation(x, b))
            writer.add_summary(summary_str, x)
