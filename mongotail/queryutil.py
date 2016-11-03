
# added
def get_index(mongo_version, obj):
    # print(obj)
    if mongo_version < '3.0':
        if 'children' in obj:
            stage = get_index(mongo_version, obj['children'])
        else:
            stage = obj['type']
            if stage == 'IXSCAN':
                stage += ': %s' % obj['keyPattern']

    else:
        if 'inputStage' in obj:
            stage = get_index(mongo_version, obj['inputStage'])
        else:
            stage = obj['stage']
            if stage == 'IXSCAN':
                stage += ': %s' % obj['keyPattern']

    return stage