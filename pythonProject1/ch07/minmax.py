def maxmin(data):
    """
    입력받은 데이터는 리스트 이다.
    입력받은 데이터의 최대값과 최소값을 리턴 하시오
    """
    result = {}
    result['max'] = max(data)
    result['min'] = min(data)
    return result
if __name__ == '__main__':
    data = [5,7,2,6,2,3,9]
    result = maxmin(data)
    print(result['max'])
    print(result['min'])