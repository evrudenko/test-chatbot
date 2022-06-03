# for intent catcher
with tf.compat.v1.Session() as session:
    session.run([tf.compat.v1.global_variables_initializer(),
                 tf.compat.v1.tables_initializer()])
    test_embeddings = session.run(use(utterances))
