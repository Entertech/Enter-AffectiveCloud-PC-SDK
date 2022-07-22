AffectiveServiceType = str


class AffectiveServices(object):

    # Base Service EEG required:
    ATTENTION: AffectiveServiceType = 'attention'
    ATTENTION_FOR_CHILD: AffectiveServiceType = 'attention_chd'
    RELAXATION: AffectiveServiceType = 'relaxation'
    RELAXATION_FOR_CHILD: AffectiveServiceType = 'relaxation_chd'
    PLEASURE: AffectiveServiceType = 'pleasure'
    SLEEP: AffectiveServiceType = 'sleep'

    # Base Service HR required:
    PRESSURE: AffectiveServiceType = 'pressure'
    AROUSAL: AffectiveServiceType = 'arousal'
    COHERENCE: AffectiveServiceType = 'coherence'
