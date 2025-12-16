em_sal = list(map(int, input("Enter the employee salaries separated by spaces: ").split()))
m_x = max(em_sal)
m_n = min(em_sal)
print(m_x - m_n)