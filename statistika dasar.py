class data:

    def __init__(self,data):
        self.data = data
    
    def mean(self):
        datasum = sum(self.data)
        datalength = len(self.data)
        return datasum/datalength

    def median(self):
        sorteddata=sorted(self.data)
        if len(sorteddata)%2==0:
            i=int((len(sorteddata)-2)/2)
            return (sorteddata[i+1]+sorteddata[i])/2
        else:
            i=len(sorteddata)-1
            return sorteddata[round(i/2)]
    
    def modus(self):
        cutteddata=list(dict.fromkeys(self.data))
        freq = [self.data.count(x) for x in cutteddata]
        return cutteddata[freq.index(max(freq))]

    def kuartil_satu(self):
        sorteddata=sorted(self.data)
        if len(self.data)%2==0:
            data = sorteddata[:round(len(self.data)/2)]
            if len(data)%2==0:
                i=int((len(data)-2)/2)
                return (data[i+1]+data[i])/2
            else:
                i=len(data)-1
                return data[round(i/2)]
        else:
            data = sorteddata[:round((len(self.data)-1)/2)]
            if len(data)%2==0:
                i=int((len(data)-2)/2)
                return (data[i+1]+data[i])/2
            else:
                i=len(data)-1
                return data[round(i/2)]
    
    def kuartil_dua(self):
        return self.median()

    def kuartil_tiga(self):
        sorteddata=sorted(self.data)
        if len(self.data)%2==0:
            data = sorteddata[-round(len(self.data)/2):]
            if len(data)%2==0:
                i=int((len(data)-2)/2)
                return (data[i+1]+data[i])/2
            else:
                i=len(data)-1
                return data[round(i/2)]
        else:
            data = sorteddata[-round((len(self.data)-1)/2):]
            if len(data)%2==0:
                i=int((len(data)-2)/2)
                return (data[i+1]+data[i])/2
            else:
                i=len(data)-1
                return data[round(i/2)]

    def jangkauan(self):
        datamax = max(self.data)
        datamin = min(self.data)
        return datamax-datamin
    
    def simpangan_quartil(self):
        return self.kuartil_tiga()-self.kuartil_satu()

    def variansi(self):
        return sum([(i-self.mean())**2 for i in self.data])/len(self.data)

    def standar_deviasi(self):
        return self.variansi()**0.5

