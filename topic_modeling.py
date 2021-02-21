from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

def print_top_words(model, feature_names, n_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print("Topic #%d:" % topic_idx)
        print(" ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]]))
        print()

def lda_topic_modeling(text, max_df_lda=0.15,min_df_lda=5, topics_number = 5, max_iter=200):
    tf_vectorizer = CountVectorizer(max_df=max_df_lda,min_df=min_df_lda)
    tf = tf_vectorizer.fit_transform(text)
    lda = LatentDirichletAllocation(n_components=topics_number, max_iter=max_iter, learning_method='batch')
    result_topic = lda.fit(tf)
    print(result_topic)
    n_top_words = 50
    tf_features_names = tf_vectorizer.get_feature_names()
    print_top_words(lda, tf_features_names, n_top_words)
